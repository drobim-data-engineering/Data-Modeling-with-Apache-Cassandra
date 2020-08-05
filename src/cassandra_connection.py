from cassandra.cluster import Cluster

def create_connection():
    try:
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect()
        return session
    except Exception as e:
        print(e)   
        
def create_keyspace(session,keyspace):
    try:
        query = """
        CREATE KEYSPACE IF NOT EXISTS """ + keyspace + """
        WITH REPLICATION = 
        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
        """
        session.execute(query)
        return keyspace
    except Exception as e:
        print(e)