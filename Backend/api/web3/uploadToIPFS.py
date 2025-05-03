import requests
import os
import json # Import json for error details

class PinataUpload:
    def uploadPinata(self, filepath, jwt_token):
        url = "https://api.pinata.cloud/pinning/pinFileTOIPFS"

        headers = {'Authorization': f'Bearer {jwt_token}'}

        try:
            with open(filepath, 'rb') as f:
                response = requests.post(url, files={'file': f}, headers=headers)

            response.raise_for_status() 
            return response.json()

        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred during Pinata upload: {e}")
            try:
                 error_details = response.json()
                 print(f"Pinata API Error Details: {error_details}")
                 return {"error": error_details}
            except json.JSONDecodeError:
                 print("Could not decode Pinata error response body as JSON.")
                 return {"error": response.text}

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during Pinata upload: {e}")
            return {"error": str(e)}

        except FileNotFoundError:
             print(f"Error: File not found at {filepath} for Pinata upload.")
             return {"error": "File not found"}

# You might want to instantiate this once globally or pass it if using dependency injection
# pinata_uploader_instance = PinataUpload()