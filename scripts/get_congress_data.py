import pandas as pd


senate_table_name = 'senate_members'
house_table_name = 'house_members'


def drop_table(table_name, cursor):
    # Create the table if it doesn't exist
    cursor.execute(f'''
        ''')


def recreate_house_table(cursor):
    cursor.execute(f'''
        DROP TABLE IF EXISTS {house_table_name};
    ''')
    # Create the table if it doesn't exist
    cursor.execute(f'''
        CREATE TABLE {house_table_name} (
        id TEXT PRIMARY KEY,
        title TEXT,
        short_title TEXT,
        api_uri TEXT,
        first_name TEXT,
        middle_name TEXT,
        last_name TEXT,
        suffix TEXT,
        date_of_birth DATE,
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
        in_office BOOLEAN,
        cook_pvi TEXT,
        dw_nominate REAL,
        ideal_point REAL,
        seniority INTEGER,
        next_election INTEGER,
        total_votes INTEGER,
        missed_votes INTEGER,
        total_present INTEGER,
        last_updated TEXT,
        ocd_id TEXT,
        office TEXT,
        phone TEXT,
        fax TEXT,
        state TEXT,
        district TEXT,
        at_large BOOLEAN,
        geoid TEXT,
        missed_votes_pct REAL,
        votes_with_party_pct REAL,
        votes_against_party_pct REAL
    );
    ''')
    return house_table_name


def recreate_senate_table(cursor):
    # Create the table if it doesn't exist
    cursor.execute(f'''
        DROP TABLE IF EXISTS {senate_table_name};
    ''')
    cursor.execute(f'''
        CREATE TABLE {senate_table_name} (
        id TEXT PRIMARY KEY,
        title TEXT,
        short_title TEXT,
        api_uri TEXT,
        first_name TEXT,
        middle_name TEXT,
        last_name TEXT,
        suffix TEXT,
        date_of_birth DATE,
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
        in_office BOOLEAN,
        cook_pvi TEXT,
        dw_nominate REAL,
        ideal_point REAL,
        seniority INTEGER,
        next_election INTEGER,
        total_votes INTEGER,
        missed_votes INTEGER,
        total_present INTEGER,
        last_updated TEXT,
        ocd_id TEXT,
        office TEXT,
        phone TEXT,
        fax TEXT,
        state TEXT,
        senate_class INTEGER,
        state_rank TEXT,
        lis_id TEXT,
        missed_votes_pct REAL,
        votes_with_party_pct REAL,
        votes_against_party_pct REAL
    );
    ''')
    return senate_table_name


def add_members_to_db(members, table, conn):
    # Create a Pandas DataFrame from the extracted data
    df = pd.DataFrame(members)

    # Assuming df is your DataFrame and "id" is the primary key
    df.to_sql(table, conn, if_exists="append", index=False, index_label="id")

