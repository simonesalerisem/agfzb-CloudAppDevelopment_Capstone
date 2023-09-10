from cloudant import Cloudant
from cloudant.error import CloudantException
import requests

def post_review_to_db(account_name, api_key, review_data):
    try:
        client = Cloudant.iam(
            account_name=account_name,
            api_key=api_key,
            connect=True,
        )
        db = client['reviews']
        
        document = db.create_document(review_data)  # Create a new document with the review data

        if document.exists():
            return {"message": "Review successfully posted"}
        else:
            return {"error": "Failed to post review"}

    except CloudantException as cloudant_exception:
        print("Unable to connect to the database.")
        return {"error": str(cloudant_exception)}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("Connection error.")
        return {"error": str(err)}