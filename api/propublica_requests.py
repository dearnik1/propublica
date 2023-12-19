import requests
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

CONGRESS = '118'
API_URL = f"https://api.propublica.org/congress/v1"
API_KEY = os.environ['API_KEY']
if API_KEY is None:
    raise ValueError("API_KEY environment variable is not set.")
headers = {
    "X-API-Key": API_KEY,
}
print_responses = True


def get_senate_members():
    response = requests.get(f"{API_URL}/{CONGRESS}/senate/members.json", headers=headers)
    if print_responses:
        print_response(response)
    return extract_members_from_json_response(response)


def get_house_members():
    response = requests.get(f"{API_URL}/{CONGRESS}/house/members.json", headers=headers)
    if print_responses:
        print_response(response)
    return extract_members_from_json_response(response)


def get_votes_by_member(member_id):
    response = requests.get(f"{API_URL}/members/{member_id}/votes.json", headers=headers)
    if print_responses:
        print_response(response)
    return extract_votes_from_json_response(response)


def extract_members_from_json_response(response):
    if response.status_code != 200:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        return None

    # Convert the JSON response to a Python dictionary
    api_data = response.json()

    # Extract the relevant data from the outer layers
    members = api_data.get('results', [])[0].get('members', [])
    return members


def extract_votes_from_json_response(response):
    if response.status_code != 200:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        return None

    # Convert the JSON response to a Python dictionary
    api_data = response.json()

    # Extract the relevant data from the outer layers
    votes = api_data.get('results', [])[0].get('votes', [])
    return votes


def print_response(response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        json_response = response.json()
        pretty_json = json.dumps(json_response, indent=2)
        print(pretty_json)
    else:
        print(f"Error: {response.status_code}")
