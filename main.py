import requests
import sqlite3
from dotenv import load_dotenv
import os
import json
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

CONGRESS = '118'
API_URL = f"https://api.propublica.org/congress/v1/{CONGRESS}"
# DB_FILE = "congress.db"
API_KEY = os.environ['API_KEY']
if API_KEY is None:
    raise ValueError("API_KEY environment variable is not set.")
headers = {
    "X-API-Key": API_KEY,
}


def get_senate_members():
    response = requests.get(f"{API_URL}/senate/members.json", headers=headers)
    return response


def print_response(response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        json_response = response.json()
        pretty_json = json.dumps(json_response, indent=2)
        print(pretty_json)
    else:
        print(f"Error: {response.status_code}")


def main():
    api_data = get_senate_members()
    print_response(api_data)


if __name__ == "__main__":
    main()
