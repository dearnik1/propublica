import requests
import sqlite3
from datetime import datetime
CONGRESS = '118'
API_URL = "https://api.propublica.org/congress/v1/"
DB_FILE = "congress.db"

def fetch_data():
    response = requests.get(API_URL)
    return response.json()

def main():
    api_data = fetch_data()
    print(api_data)

if __name__ == "__main__":
    main()