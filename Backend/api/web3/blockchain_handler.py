import os
import json
import hashlib
from web3 import Web3
from eth_account import Account
from web3.exceptions import TransactionNotFound, ContractLogicError
from pathlib import Path

current_dir = Path(__file__).resolve()
parent_dir = current_dir.parents[0]

HOLESKY_RPC_URL = 'https://rpc.ankr.com/eth_holesky'
CONTRACT_ADDRESS = ''
BACKEND_PRIVATE_KEY = ''
ABI_FILE_PATH = f'{parent_dir}/SimpleBackendRegistry.abi'
CONTRACT_ABI = None

try:
    with open(ABI_FILE_PATH, "r") as f:
        CONTRACT_ABI = json.load(f)
except FileNotFoundError:
    print(f"FATAL ERROR: ABI file not found at {ABI_FILE_PATH}")


w3 = None
contract = None
backend_account = None
BACKEND_ADDRESS = None

def initialize_web3():
    global w3, contract, backend_account, BACKEND_ADDRESS, CONTRACT_ABI

    if w3 is not None and w3.is_connected():
        return True

    try:
        w3 = Web3(Web3.HTTPProvider(HOLESKY_RPC_URL))
        if not w3.is_connected():
            raise ConnectionError(f"Failed to connect to Web3 RPC at {HOLESKY_RPC_URL}")
        print(f"Web3 connected to Chain ID: {w3.eth.chain_id}")

        if not BACKEND_PRIVATE_KEY or BACKEND_PRIVATE_KEY == "YOUR_BACKEND_WALLET_PRIVATE_KEY":
             print("FATAL ERROR: Backend private key is not configured.")
             return False

        backend_account = Account.from_key(BACKEND_PRIVATE_KEY)
        BACKEND_ADDRESS = backend_account.address
        print(f"Backend Wallet Address: {BACKEND_ADDRESS}")

        if not CONTRACT_ABI:
            print("FATAL ERROR: Contract ABI not loaded.")
            return False
        if not CONTRACT_ADDRESS or CONTRACT_ADDRESS == "YOUR_DEPLOYED_CONTRACT_ADDRESS":
            print("FATAL ERROR: Contract address is not configured.")
            return False

        contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
        print(f"Smart Contract loaded: {CONTRACT_ADDRESS}")

        return True

    except Exception as e:
        print(f"FATAL ERROR: Web3 Initialization failed: {e}")
        w3 = None
        contract = None
        backend_account = None
        BACKEND_ADDRESS = None
        return False

def hash_user_id_to_bytes32(user_id_string):
    user_id_str = str(user_id_string)
    hashed_bytes = hashlib.sha256(user_id_str.encode('utf-8')).digest()
    return hashed_bytes

def store_report_hash_on_chain(user_unique_id, ipfs_cid):
    if not w3 or not w3.is_connected() or not contract or not backend_account:
        print("Web3 is not initialized or connected. Cannot send transaction.")
        return None, "Web3 not initialized or connected"

    try:
        user_id_hash = hash_user_id_to_bytes32(user_unique_id)
        print(f"Preparing to store CID {ipfs_cid} for hashed user ID: {user_id_hash.hex()}")

        nonce = w3.eth.get_transaction_count(BACKEND_ADDRESS)
        print(f"Using nonce: {nonce}")

        gas_price = w3.eth.gas_price
        print(f"Current gas price: {w3.from_wei(gas_price, 'gwei')} Gwei")

        transaction = contract.functions.storeReportHash(
            user_id_hash,
            ipfs_cid
        ).build_transaction({
            'chainId': w3.eth.chain_id,
            'gasPrice': gas_price,
            'from': BACKEND_ADDRESS,
            'nonce': nonce,
        })

        signed_txn = backend_account.sign_transaction(transaction)
        print("Transaction signed.")

        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"Transaction sent. Hash: {tx_hash.hex()}")

        try:
             print("Waiting for transaction confirmation...")
             transaction_receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
             print(f"Transaction confirmed in block {transaction_receipt.blockNumber}")
             if transaction_receipt.status == 1:
                 print("Transaction successful.")
                 return tx_hash.hex(), None
             else:
                 print("Transaction failed on chain (status != 1).")
                 return None, f"Transaction failed on chain, receipt status: {transaction_receipt.status}"

        except TransactionNotFound:
             print("Transaction not found after waiting (might still be pending).")
             return tx_hash.hex(), "Transaction sent but timed out waiting for confirmation"

        except Exception as receipt_e:
             print(f"Error while waiting for transaction receipt: {receipt_e}")
             return tx_hash.hex(), f"Transaction sent but error waiting for receipt: {receipt_e}"


    except ContractLogicError as e:
         print(f"Smart contract reverted transaction: {e}")
         return None, f"Smart contract execution failed: {e}"

    except Exception as e:
        print(f"An error occurred during blockchain transaction: {e}")
        return None, f"Failed to send blockchain transaction: {e}"

def get_stored_cid(user_unique_id):
    if not w3 or not w3.is_connected() or not contract or not BACKEND_ADDRESS:
        print("Web3 is not initialized or connected. Cannot retrieve data.")
        return None, "Web3 not initialized or connected"

    try:
        user_id_hash = hash_user_id_to_bytes32(user_unique_id)
        print(f"Querying CID for hashed user ID: {user_id_hash.hex()}")

        stored_cid = contract.functions.backendReports(BACKEND_ADDRESS, user_id_hash).call()

        print(f"Retrieved CID: {stored_cid}")
        if not stored_cid:
            return None, "No CID found for this user ID under the backend address."

        return stored_cid, None 

    except Exception as e:
        print(f"An error occurred during data retrieval: {e}")
        return None, f"Failed to retrieve CID: {e}"
    
