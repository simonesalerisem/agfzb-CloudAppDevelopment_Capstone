from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests

def get_reviews(account_name, api_key, dealership=None):
    try:
        client = Cloudant.iam(
            account_name=account_name,
            api_key=api_key,
            connect=True,
        )
        db = client['reviews']
        reviews = []

        dealerId = None  # Initialize dealerId to None

        if dealership is not None:
            dealerId = int(dealership)  # Convert dealerId to integer

        for document in db:
            # If dealerId is provided, only add reviews for that dealership
            if dealerId is None or document.get('dealership') == dealerId:
                reviews.append(document)

    except CloudantException as cloudant_exception:
        print("Unable to connect to the database.")
        return {"error": cloudant_exception}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("Connection error.")
        return {"error": err}

    return {"reviews": reviews}