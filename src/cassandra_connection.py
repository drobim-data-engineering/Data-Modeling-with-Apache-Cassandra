from cassandra.cluster import Cluster

# Define Namespace
keyspace = 'udacity'

def create_connection():
    """Function to create Cassandra Connection

    Returns:
        [cassandra.cluster.Session]: A Cassandra Session on a Cassandra Cluster
    """
    try:
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect()
        return session
    except Exception as e:
        print(e)

def create_keyspace(session,keyspace):
    """Function to create a Cassandra Keyspace

    Args:
        session ([cassandra.cluster.Session]): [A Cassandra Session on a Cassandra Cluster]
        keyspace ([string]): [Keyspace Name]
    """
    try:
        query = '''
        CREATE KEYSPACE IF NOT EXISTS ''' + keyspace + '''
        WITH REPLICATION =
        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
        '''
        session.execute(query)
    except Exception as e:
        print(e)