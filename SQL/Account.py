import sqlite3
import bcrypt
import hashlib
import hmac

global user_name

def checkuser(cursor,user_name) -> bool:
   cursor.execute(
            "Select 1 FROM Users WHERE username = ? LIMIT 1",
            (user_name,)
        )
   result = cursor.fetchone()
   return result is not None

def hash_password(username, password, salt) -> str:
    # Combine username and password before hashing
    combined_input = f"{username}:{password}"
    pepper = f"{'SzymonNEA2024'}:{username}"
    hashed_input = hmac.new(pepper.encode('utf-8'),combined_input.encode('utf-8'), hashlib.sha256).hexdigest()
    # Hash the combined input
    hashed_password = bcrypt.hashpw(hashed_input.encode('utf-8'),salt)
    # Return hashed password
    return hashed_password.decode('utf-8')

def create_User(user_name,password):
    try:
        conn = sqlite3.connect("SIGNIT2.db")
        cursor = conn.cursor()
        if not checkuser(cursor, user_name):
            salt = bcrypt.gensalt()
            Hashpassword = hash_password(user_name,password,salt)
            cursor.execute("INSERT INTO Users (username, password,Salt) VALUES(?,?,?)",(user_name, Hashpassword, salt)        )
            conn.commit()
        else:
            print("Can't") #get rid of this

    except sqlite3.Error as error:
        print("Error") #get rid of this
    
    finally:
        conn.close()

def Login(user_name,password):
    try:
        conn = sqlite3.connect("SIGNIT2.db")
        cursor = conn.cursor()
        if checkuser(cursor, user_name):
            cursor.execute("SELECT password,Salt FROM Users WHERE username = ?", 
                           (user_name,))
            result = cursor.fetchone()
            print(result)
            hashedpassword, salt = result
            hashpass = hash_password(user_name,password, salt)
            if hashpass == hashedpassword:
                LoggedIn()
            else:
                FailedLogin()
         
        else:
            print("Can't") #get rid of this

    except sqlite3.Error as error:
        print("Error") #get rid of this
    
    finally:
        conn.close()

def LoggedIn():
    print("in")

    
def FailedLogin():
    print("Cant")

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





        
        



