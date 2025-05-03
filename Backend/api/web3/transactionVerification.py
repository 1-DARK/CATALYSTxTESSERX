# Using web3.py
from web3 import Web3

class Verify:
    def trxn_verify(self, hash):
        web3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth_holesky"))
        receipt = web3.eth.get_transaction_receipt(str(hash))
        return receipt
