from rest_framework.response import Response
from rest_framework import parsers
from rest_framework.decorators import api_view, parser_classes
from base.models import Img
from .serializers import ImgSerializer, VideoSerializer, PdfSerializer
from .services import llm_handler, image_handler, video_handler
from django.http import JsonResponse, HttpResponse
import json
from .prettify import prettify
from .web3 import pdfencrypt, uploadToIPFS
from .web3.blockchain_handler import store_report_hash_on_chain, initialize_web3, w3
from .web3.transactionVerification import Verify
import hashlib

@api_view(['POST'])
def query(request):
    print(request.data)
    question = request.data['content']
    Q = llm_handler.QueryResponse()
    responseFromLLM = Q.generateResponse(question)
    prettifiedStr = prettify.Prettify()
    prettyString = prettifiedStr.prettify_llm_json_string(responseFromLLM)
    count = 0
    for i in prettyString:
        if i == '<':
            break
        count += 1
    prettyString = prettyString[count:]
    print(prettyString)
    # resDict = {'response': f'{prettyString}'}
    return HttpResponse(prettyString, status=200)


@api_view(['POST'])
def PdfViewSet(request):
    pdf_name = request.data['file']
    print(pdf_name)
    serializer = PdfSerializer(data=request.data)
    if serializer.is_valid():
        ipfs_cid = None
        pinata_upload_error = None
        serializer.save()
        request.session.save()
        user_unique_id = request.session.session_key
        e = pdfencrypt.EncryptPdf()
        encryption_key_string = hashlib.sha256(user_unique_id.encode()).hexdigest()[:32]
        
        loc = e.encrypt(pdf_name)
        jwt = ''
        p = uploadToIPFS.PinataUpload()
        pinata_result = p.uploadPinata(loc, jwt)
        print(pinata_result)
        if pinata_result and 'IpfsHash' in pinata_result:
            ipfs_cid = pinata_result['IpfsHash']
            print(f"Pinata upload successful, CID: {ipfs_cid}")
        else:
            pinata_upload_error = f"Pinata API Error: {pinata_result.get('error', 'Unknown error details')}"
            print(f"Pinata upload failed: {pinata_upload_error}")
        
        tx_hash = None
        blockchain_storage_error = None

        from .web3.blockchain_handler import w3
        if ipfs_cid:
            if w3 and w3.is_connected():
                print(f"Attempting to store CID {ipfs_cid} on chain for user ID: {user_unique_id}")

                tx_hash, blockchain_storage_error = store_report_hash_on_chain(user_unique_id, ipfs_cid)

                if tx_hash:
                    print(f"Blockchain transaction initiated: {tx_hash}")
                else:
                    print(f"Failed to initiate blockchain transaction: {blockchain_storage_error}")
            else:
                print("Web3 not initialized/connected. Skipping blockchain storage.")
                blockchain_storage_error = "Web3 not initialized/connected. Check server logs."

        else:
            print("Skipping blockchain storage as IPFS CID is not available.")
            

        response_data = {
            "status": "Processing Complete", 
            "user_id_for_verification": user_unique_id, 
            "encryption_key_derived": encryption_key_string, 
            "ipfs_upload": {
                "success": ipfs_cid is not None,
                "cid": ipfs_cid,
                "error": pinata_upload_error,
                "ipfs_gateway_url": f"https://ipfs.io/ipfs/{ipfs_cid}" if ipfs_cid else None # Helpful URL
            },
            "blockchain_storage": {
                "success": tx_hash is not None,
                "tx_hash": tx_hash,
                "error": blockchain_storage_error,
                "block_explorer_url": f"https://holesky.etherscan.io/tx/{tx_hash}" if tx_hash else None # Helpful URL
            }
        }

        http_status = 201 
        if ipfs_cid is None: 
            http_status = 500 

        return JsonResponse(response_data, status=http_status)


@api_view(['POST'])
def VerifyTxn(request):
    trxn_hash = request.data['hash']
    print(trxn_hash)
    v = Verify()
    trxn_data = v.trxn_verify(trxn_hash)
    trxn_data = dict(trxn_data)
    resDict = {'response': f'{trxn_data}'}
    print(resDict)
    print(JsonResponse(resDict, status=201))
    return JsonResponse(resDict, status=201)
