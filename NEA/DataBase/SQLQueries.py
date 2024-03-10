import sqlite3
from datetime import datetime
from Interface import Notifications

notificationhandler = Notifications.NotificationHandler

''' 
    Opens a connection to the database
    
    Returns:
        cursor (sqlite3.Cursor): cursor for executing SQL queries
        conn (sqlite3.Connection): connection to the database
'''
def DBopenner():
    conn = sqlite3.connect("DataBase\SIGNIT2.db")
    cursor = conn.cursor()
    return cursor, conn


'''
    Checks if a user exists whithin the Users table
    
    Parameter:
        user_name(str): username to check

    Returns:
        bool: true if the user exists
'''
def checkuser(user_name) -> bool:
    cursor, conn = DBopenner()
    cursor.execute(
            "Select 1 FROM Users WHERE username = ? LIMIT 1",
            (user_name,)
        )
    result = cursor.fetchone()
    return result is not None

'''
    Executes SQL queries for account creation and login

    Parameters:
          Query(str): SQL query to execute
          parameters(tuple) for the query
          Setting(str): "Create" for account creation or "Login" to login

    Return:
        Str or tuple: result message or login information
'''
def AccountSQLExecutor(Query,parameters,Setting):
    try:
        cursor, conn = DBopenner()
        cursor.execute(Query, parameters)
        conn.commit()
        if(Setting=="Create"):
            return "Account sucessfully created\n you can now login"
        elif(Setting=="Login"):
            result = cursor.fetchone()
            hashedpassword, salt = result
            return hashedpassword, salt
    except sqlite3.Error as error:
        notificationhandler.trigger_notification("There has been an error when trying to connect to the database",1,"warning")
    finally:
        if conn:
            conn.close()

'''
    Retrieves word data from the database table

    Returns:
        list of tuples containing word data
'''
def wordGetter():
    try:
        cursor, conn = DBopenner()
        cursor.execute("""SELECT 
                                word_name, 
                                Cat_name, 
                                download_link
                          FROM Categories AS C
                          JOIN Words AS W ON C.Cat_ID = W.Cat_ID""")
        word_data = cursor.fetchall()
        return word_data
    except sqlite3.Error as error:
        notificationhandler.trigger_notification("There has been an error when trying to connect to the database",1,"warning")
    
    finally:
        if conn:
            conn.close()

'''
    Gets the attempt count and most recent attempt data for a user attempt at a word from database

    Parameters:
        username(str): the username to lookup
        word_name(str): the word name

    Returns:
        tuple: attempt count and most recent attempt date or none if nothing matches
'''
def AttemptGetter(username,word_name):
    try:
        cursor, conn = DBopenner()
        query = """
            SELECT COUNT(UserWords.User_id) AS attempt_count, MAX(UserWords.DateOfAttempt) AS most_recent_date
            FROM UserWords
            JOIN Users ON UserWords.User_id = Users.User_id
            JOIN Words ON UserWords.word_id = Words.word_id
            WHERE Users.username = ? AND Words.word_name = ?

        """
        cursor.execute(query, (username, word_name))
        result = cursor.fetchone()
        return result
    except sqlite3.Error as error:
        notificationhandler.trigger_notification("There has been an error when trying to connect to the database",1,"warning")
    
    finally:
        if conn:
            conn.close()

'''
    Adds a new attempt for a user and word
    
    Parameters:
        username(str): the username to add an entry for
        word_name(str): the word_name to add entry for
'''
def AddAttempt(username, word_name):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor, conn = DBopenner()

        # Insert into UserWords table
        insert_query = """
            INSERT INTO UserWords (User_id, word_id, DateOfAttempt)
            SELECT Users.User_id, Words.word_id, ?
            FROM Users, Words
            WHERE Users.username = ? AND Words.word_name = ?
        """
        cursor.execute(insert_query, (current_date, username, word_name))
        conn.commit()

    except sqlite3.Error as error:
        notificationhandler.trigger_notification("There has been an error when trying to connect to the database", 1, "warning")

    finally:
        if conn:
            conn.close()
    

