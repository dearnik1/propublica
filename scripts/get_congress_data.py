import pandas as pd


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


def add_members_to_db(members, conn):
    # Create a Pandas DataFrame from the extracted data
    df = pd.DataFrame(members)

    # Insert or replace data into the existing table using Pandas to_sql
    df.to_sql("congress", conn, if_exists="replace", index=False)
