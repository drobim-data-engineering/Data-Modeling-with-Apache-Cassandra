from cassandra_connection import *
from cql_queries import *
import sys

# Creates Dictionary with all available questions
questions = {
              1: "1. Give me the artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4"
             ,2: "2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182"
             ,3: "3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'"
            }

def get_question(question_number):
    """Function to return the question from a dictionary

    Args:
        question_number (int): The question number you want to answer
    """
    print('\n' + questions.get(question_number,"Invalid question number!") + '\n')

def main():
    """"
    Script entry point, following these steps:
        1. Requests user to input a value according to the question number
        2. Valids user input
        3. Creates connection to Cassandra Cluster
        4. Creates Cassandra Keyspace
        5. Sets up Cassandra Keyspace
        6. Executes CQL Query according to input by user
        7. Prints the results
    The script will run until the user requests to exit, by pressing 0.
    Args:
        None
    Returns:
        None
    """

    # Prints the questions available
    print("""
    These are the available questions you can answer:

    1. Give me the artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4
    2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
    3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

    """)

    # Creates an empty list to validate inputs by user
    question_list = list(questions.keys())

    # Calls for an infinite loop that keeps executing until user enter a valid question number
    while True:

            # Try to convert the input to a integer, If something else that is not a number is introduced the ValueError exception will be called.
            try:
                question_number = int(input("Please enter the QUESTION NUMBER you want to answer or [0] to exit: "))
                if question_number == 0:
                    print('Exiting Validation Script... Goodbye! \n')
                    sys.exit()
                elif question_number not in question_list:
                    print("Error! This is not a valid question number. These are valids QUESTION NUMBER {} ".format(question_list))
                else:
                    # Connects to Cassandra
                    session = create_connection()

                    # Creates Keyspace
                    create_keyspace(session,keyspace)

                    # Sets Keyspace
                    session.set_keyspace(keyspace)

                    #Get Query By Question Number
                    query = get_query(question_number)

                    #Print Question
                    get_question(question_number)

                    #Execute Query
                    rows = session.execute(query)
                    for row in rows:
                        print(row)
                    print('\n')

            # This is the exception called the attempt to convert the input to integer
            except ValueError:
                # The cycle will go on until validation
                print("Error! This is not a number. Try again.")

if __name__ == '__main__':
    main()






