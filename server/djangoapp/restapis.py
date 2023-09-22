import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
        print(kwargs)
        print("GET from {} ".format(url))
        try:
            response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
        except requests.exceptions.RequestException as e:
            print(f"Network exception occurred: {e}")
            return None

        print(response.text)
        status_code = response.status_code
        print("With status {} ".format(status_code))

        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data
        else:
            return None


def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)

    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result['result']
        # For each dealer object
        for dealer in dealers:
          #Get its content in `doc` object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)
            

    return results

def get_dealer_reviews_from_cf(url, dealer_id):
    results = []
    
    # Call get_request with a URL
    json_result = get_request(url)

    if json_result:
        # Get the row list in JSON as reviews
        reviews = json_result['result']
        
        # For each review object
        for review in reviews:
            # Get its content in `doc` object
            review_doc = review["doc"]
            
            # Check if the dealership id in the review matches the provided dealer_id
            if review_doc["id"] == dealer_id:

                sentiment_default = "basic_sentiment"
                
                # Create a DealerReview object with values in `doc` object
                review_obj = DealerReview(dealership=review_doc["dealership"], 
                                          name=review_doc["name"], 
                                          purchase=review_doc["purchase"],
                                          purchase_date=review_doc["purchase_date"],
                                          review=review_doc["review"],
                                          car_make=review_doc["car_make"],
                                          car_model=review_doc["car_model"],
                                          car_year=review_doc["car_year"],
                                          sentiment=sentiment_default,
                                          id=review_doc["id"])

                results.append(review_obj)

    return results

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



