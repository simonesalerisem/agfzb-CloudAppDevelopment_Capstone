from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests

def get_dbs(account_name, api_key):
    try:
        client = Cloudant.iam(
            account_name=account_name,
            api_key=api_key,
            connect=True,
        )
        print(f"Databases: {client.all_dbs()}")
    except CloudantException as cloudant_exception:
        print("unable to connect")
        return {"error": cloudant_exception}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"dbs": client.all_dbs()}