import sqlite3
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
        conn.close()

def GetavgperCat(cursor,user_name) -> str:
    cursor.execute("""SELECT
                          C.Cat_name,
                          AVG(UW.accuracy) AS AvgAccuracy
                      FROM
                         Categories AS C
                      JOIN
                         Words AS W ON C.Cat_ID = W.Cat_ID
                      JOIN
                         UserWords AS UW ON W.word_id = UW.word_id
                      JOIN
                         Users AS U ON UW.User_id = U.User_id
                      WHERE
                         U.username = ?
                      GROUP BY
                         C.Cat_name""", 
                                      (user_name,))
    avgpCat = cursor.fetchall()
    return avgpCat

def GetProgress(user_name):
    try:
        conn = sqlite3.connect("SIGNIT2.db")
        cursor = conn.cursor()
        if checkuser(cursor, user_name):
            cursor.execute("""SELECT
                                    C.Cat_name,
                                    W.word_name,
                                    UW.accuracy,
                                    UW.NoAttempts
                                FROM
                                    Categories AS C
                                JOIN
                                    Words AS W ON C.Cat_ID = W.Cat_ID
                                JOIN
                                    UserWords AS UW ON W.word_id = UW.word_id
                                JOIN
                                    Users AS U ON UW.User_id = U.User_id
                                WHERE
                                    U.username = ?""", 
                                                     (user_name,))
            result = cursor.fetchall()
            for row in result:
                print(row)
            avgpCat = GetavgperCat(cursor,user_name)
            for row in avgpCat:
                print(row)
        else:
            print("Can't") #get rid of this

    except sqlite3.Error as error:
        print("Error") #get rid of this
    
    finally:
        conn.close()

