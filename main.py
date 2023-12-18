import sqlite3
from scripts.get_congress_data import *
from api.propublica_requests import *

DB_FILE = "congress.db"


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
