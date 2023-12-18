import requests
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

CONGRESS = '118'
API_URL = f"https://api.propublica.org/congress/v1/{CONGRESS}"
API_KEY = os.environ['API_KEY']
if API_KEY is None:
    raise ValueError("API_KEY environment variable is not set.")
headers = {
    "X-API-Key": API_KEY,
}


def get_senate_members():
    response = requests.get(f"{API_URL}/senate/members.json", headers=headers)
    return get_members_list_from_json_response(response)


def get_house_members():
    response = requests.get(f"{API_URL}/house/members.json", headers=headers)
    return get_members_list_from_json_response(response)


def get_members_list_from_json_response(response):
    if response.status_code != 200:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        return None

    # Convert the JSON response to a Python dictionary
    api_data = response.json()

    # Extract the relevant data from the outer layers
    members = api_data.get('results', [])[0].get('members', [])
    return members


def print_response(response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        json_response = response.json()
        pretty_json = json.dumps(json_response, indent=2)
        print(pretty_json)
    else:
        print(f"Error: {response.status_code}")
