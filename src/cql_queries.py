import cassandra
import pandas as pd

def create_tables(session):
    """Function to create tables on Cassandra

    Args:
        session (cassandra.cluster.Session): [A Cassandra Session on a Cassadra Cluster]
    """
    for query in create_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)

def insert_data(session, query, df, df_columns):
    """Function to insert data into a table on a Cassandra Cluster

    Args:
        session (cassandra.cluster.Session): [A Cassandra Session on a Cassadra Cluster]
        query (string): [Insert Into CQL Query]
        df (DataFrame): [description]
        df_columns (list): [description]
    """
    for i, row in df.iterrows():
        data = tuple([row[col] for col in df_columns])
        session.execute(query, data)

def get_query(question_number):
    """Function to return a CQL query based on a question number

    Args:
        question_number ([int]): [Question number the user wants to answer]

    Returns:
        [string]: [CQL Query]
    """
    query = {
              1: "select artist_name, song_title, song_length from song_details_itemInSession where session_id = 338 and itemInSession = 4"
             ,2: "select artist_name, song_name, user_firstName, user_lastName from song_playlist_session where userid = 10 and sessionid = 182"
             ,3: "select user_firstName, user_lastName from user_list_by_song where song_title = 'All Hands Against His Own'"
            }
    return query.get(question_number,"Invalid question number!")

song_details_itemInSession_create = """
    CREATE TABLE IF NOT EXISTS song_details_itemInSession
    (session_id int, itemInSession int, artist_name text, song_title text, song_length float
    ,PRIMARY KEY(session_id, itemInSession))
"""

song_playlist_session_create = """
    CREATE TABLE IF NOT EXISTS song_playlist_session
    (userId int, sessionId int, itemInSession int, artist_name text, song_name text, user_firstName text, user_lastName text
    ,PRIMARY KEY((userId, sessionId), itemInSession))
"""

user_list_by_song_create = """
    CREATE TABLE IF NOT EXISTS user_list_by_song
    (song_title text, userId int, artist_name text, user_firstName text, user_lastName text
    ,PRIMARY KEY(song_title, userId))
"""

song_details_itemInSession_insert = """
    INSERT INTO song_details_itemInSession(session_id, itemInSession, artist_name, song_title, song_length)
    VALUES(%s, %s, %s, %s, %s)
"""

song_playlist_session_insert = """
    INSERT INTO song_playlist_session(userId, sessionId, itemInSession, artist_name, song_name, user_firstName, user_lastName)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
"""

user_list_by_song_insert = """
    INSERT INTO user_list_by_song(song_title, userId, artist_name, user_firstName, user_lastName)
    VALUES(%s, %s, %s, %s, %s)
"""

create_table_queries = [song_details_itemInSession_create, song_playlist_session_create, user_list_by_song_create]