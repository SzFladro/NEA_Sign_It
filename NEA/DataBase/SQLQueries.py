import sqlite3
from datetime import datetime
from Interface import Notifications

notificationhandler = Notifications.NotificationHandler

def DBopenner():
    conn = sqlite3.connect("DataBase\SIGNIT2.db")
    cursor = conn.cursor()
    return cursor, conn

#  @RETURNS True if user exists within the table 
def checkuser(user_name) -> bool:

    cursor, conn = DBopenner()
    # Searches for a username within the User table by selecting an entry if it exists
    cursor.execute(
            "Select 1 FROM Users WHERE username = ? LIMIT 1",
            (user_name,)
        )
    #if there is no user selected of that username then it will return None
    result = cursor.fetchone()
    return result is not None

#Creates the user account within the database storing their username, hashed password, salt
def AccountSQLExecutor(Query,parameters,Setting):
    try:
        cursor, conn = DBopenner()
        #establishes the connection to the database that stores user information
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

def AttemptGetter(username,word_name):
    try:
        cursor, conn = DBopenner()
        query = """
            SELECT COUNT(UserWords.User_id) AS attempt_count, MAX(UserWords.DateOfAttempt) AS most_recent_date
            FROM UserWords
            JOIN Users ON UserWords.User_id = Users.User_id
            JOIN Words ON UserWords.word_id = Words.word_id
            WHERE Users.username = "Szymon" AND Words.word_name = "A"

        """
        cursor.execute(query, (username, word_name))
        result = cursor.fetchone()
        return result
    except sqlite3.Error as error:
        notificationhandler.trigger_notification("There has been an error when trying to connect to the database",1,"warning")
    
    finally:
        if conn:
            conn.close()

def AddAttempt(username,word_name):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor, conn = DBopenner()
        cursor.execute("""
            INSERT INTO UserWords (User_id, word_id, DateOfAttempt)
            VALUES (?, ?, ?)""", (user_id, word_id, current_date))
        conn.commit()
    except sqlite3.Error as error:
        notificationhandler.trigger_notification("There has been an error when trying to connect to the database",1,"warning")
    
    finally:
        if conn:
            conn.close()
    

