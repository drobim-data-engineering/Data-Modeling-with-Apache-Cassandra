import cassandra
import pandas as pd

def create_tables(session):
    for query in create_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)

def insert_data(session, query, df, df_columns):
    for i, row in df.iterrows():
        data = tuple([row[col] for col in df_columns])
        session.execute(query, data)

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