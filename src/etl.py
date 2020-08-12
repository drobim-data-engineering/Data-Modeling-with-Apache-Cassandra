from cql_queries import *
from cassandra_connection import *
from collect_events import *
import re

def main():
    """"
    Script entry point, following these steps:
        1. Consolidates event files
        2. Creates connection to Cassandra Cluster
        3. Creates Cassandra Keyspace
        4. Sets up Cassandra Keyspace
        5. Creates Cassandra Tables
        6. Loads Data into Cassandra Tables
        7. Shuts down Cassandra Session
    Args:
        None
    Returns:
        None
    """

    # Gets the current folder and subfolder event data
    print('Consolidating event files...')

    filepath = os.getcwd() + '/event_data'

    # Get event files
    file_path_list = collect_files(filepath)
    print(f'Total Files: ' + str(len(file_path_list)))

    # Consolidates event files
    full_data_rows_list = collect_records(file_path_list)
    output_row_count = create_output_file(full_data_rows_list)

    print(f'Written {output_row_count} rows to the output file.')

    # Connects to Cassandra
    print('Connecting to Cassandra cluster...')
    session = create_connection()

    # Creates Keyspace
    print('Creating keyspace...')
    create_keyspace(session,keyspace)

    # Sets Keyspace
    print('Setting up keyspace...')
    session.set_keyspace(keyspace)

    # Creates Tables
    print('Creating tables...')
    create_tables(session)
    print('Tables created.')

    # Import event file
    file = 'event_datafile_new.csv'
    df = pd.read_csv(file, encoding='utf8')

    print('Loading data...')

    insert_data(session, song_details_itemInSession_insert, df, ['sessionId', 'itemInSession', 'artist', 'song', 'length'])
    insert_data(session, song_playlist_session_insert, df, ['userId', 'sessionId', 'itemInSession', 'artist', 'song', 'firstName', 'lastName'])
    insert_data(session, user_list_by_song_insert, df, ['song', 'userId', 'artist', 'firstName', 'lastName'])

    print('Data loaded.')

    # Shuts down cassandra session
    print('Shutting down Cassandra session...')
    session.shutdown()

    print('ETL Completed!')
    print('Please execute validation.py to validate the data')

if __name__ == '__main__':
    main()