from flask import Flask, jsonify, request
from get_dbs import get_dbs
from get_reviews import get_reviews
from post_review_to_db import post_review_to_db
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/get_dbs', methods=['GET'])
def dbs():
    account_name = "4d49b96f-55cf-4408-aa92-c8909489cff9-bluemix"
    api_key = "RivGlV8Chqh0-jAqxcI_vKV1FQj52lZIZavOu8eP5KLw"

    result = get_dbs(account_name, api_key)
    return jsonify(result)

@app.route('/api/review', methods=['GET'])
def reviews():
    account_name = "4d49b96f-55cf-4408-aa92-c8909489cff9-bluemix"
    api_key = "RivGlV8Chqh0-jAqxcI_vKV1FQj52lZIZavOu8eP5KLw"
    dealership = request.args.get('dealerId')  # Get the dealerId parameter from the request, if it exists

    result = get_reviews(account_name, api_key, dealership)
    return jsonify(result)

# New POST endpoint
@app.route('/api/review', methods=['POST'])
def post_review():
    account_name = "4d49b96f-55cf-4408-aa92-c8909489cff9-bluemix"
    api_key = "RivGlV8Chqh0-jAqxcI_vKV1FQj52lZIZavOu8eP5KLw"


    review_data = request.get_json()  # Get the review data from the request body
    result = post_review_to_db(account_name, api_key, review_data)  # Post the review data to the database

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

