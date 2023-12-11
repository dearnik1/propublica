import requests
import sqlite3
from dotenv import load_dotenv
import os
import json
import pandas as pd
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

CONGRESS = '118'
API_URL = f"https://api.propublica.org/congress/v1/{CONGRESS}"
DB_FILE = "congress.db"
API_KEY = os.environ['API_KEY']
if API_KEY is None:
    raise ValueError("API_KEY environment variable is not set.")
headers = {
    "X-API-Key": API_KEY,
}


def create_congress_table(cursor):
    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS congress (
            id TEXT PRIMARY KEY UNIQUE,
            title TEXT,
            short_title TEXT,
            api_uri TEXT,
            first_name TEXT,
            middle_name TEXT,
            last_name TEXT,
            suffix TEXT,
            date_of_birth TEXT,
            gender TEXT,
            party TEXT,
            leadership_role TEXT,
            twitter_account TEXT,
            facebook_account TEXT,
            youtube_account TEXT,
            govtrack_id TEXT,
            cspan_id TEXT,
            votesmart_id TEXT,
            icpsr_id TEXT,
            crp_id TEXT,
            google_entity_id TEXT,
            fec_candidate_id TEXT,
            url TEXT,
            rss_url TEXT,
            contact_form TEXT,
            in_office INTEGER,
            cook_pvi TEXT,
            dw_nominate REAL,
            ideal_point REAL,
            seniority TEXT,
            next_election TEXT,
            total_votes INTEGER,
            missed_votes INTEGER,
            total_present INTEGER,
            last_updated TEXT,
            ocd_id TEXT,
            office TEXT,
            phone TEXT,
            fax TEXT,
            state TEXT,
            senate_class TEXT,
            state_rank TEXT,
            lis_id TEXT,
            missed_votes_pct REAL,
            votes_with_party_pct REAL,
            votes_against_party_pct REAL
        )
    ''')


def get_senate_members():
    response = requests.get(f"{API_URL}/senate/members.json", headers=headers)
    return response


def get_house_members():
    response = requests.get(f"{API_URL}/house/members.json", headers=headers)
    return response


def print_response(response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        json_response = response.json()
        pretty_json = json.dumps(json_response, indent=2)
        print(pretty_json)
    else:
        print(f"Error: {response.status_code}")


def add_members_to_db(response, conn):
    if response.status_code != 200:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        return None

    # Convert the JSON response to a Python dictionary
    api_data = response.json()

    # Extract the relevant data from the outer layers
    members = api_data.get('results', [])[0].get('members', [])

    # Create a Pandas DataFrame from the extracted data
    df = pd.DataFrame(members)

    # Insert or replace data into the existing table using Pandas to_sql
    df.to_sql("congress", conn, if_exists="replace", index=False)


def main():
    conn = sqlite3.connect(DB_FILE)
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    create_congress_table(cursor)

    response = get_senate_members()
    add_members_to_db(response, conn)

    response = get_house_members()
    add_members_to_db(response, conn)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()
