import sqlite3
from scripts.get_congress_data import *
from api.propublica_requests import *

DB_FILE = "congress.db"
congress_table_name = 'congress'


def main():
    conn = sqlite3.connect(DB_FILE)
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    members = get_house_members()
    if members:
        table = recreate_house_table(cursor)
        add_members_to_db(members, table, conn)

    members = get_senate_members()
    if members:
        table = recreate_senate_table(cursor)
        add_members_to_db(members, table, conn)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()
