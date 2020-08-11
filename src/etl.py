from cql_queries import *
from cassandra_connection import *
from collect_events import *
import re

def validation_input(input_string):
    regex = re.compile('^[a-zA-Z]([a-zA-Z0-9_]+)*$\w{0,10}', re.I)
    match = regex.match(str(input_string))
    return bool(match)

def main():

    # Calls for an infinite loop that keeps executing until user enter a valid keyspace name
    while True:

        keyspace = input("Enter Keyspace name: ")
        validate = validation_input(keyspace)

        if validate == False:
            print("Error! This is not a valid Keyspace name, try again.")
        else:
            break

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
    keyspace_name = create_keyspace(session,keyspace)

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

if __name__ == '__main__':
    main()