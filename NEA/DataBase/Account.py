import bcrypt
import hashlib
import hmac
import re
from DataBase import config, SQLQueries
from Interface import Notifications 

notificationhandler = Notifications.NotificationHandler
config_user = config.Config()

'''
    Hashes the user password using the username and salt
    Hashes a pepper and the pepper key, adding it to the end of the hashed password

    Parameters:
        username (str): User's username
        password (str): User's password
        Salt (bytes): Unique salt assigned to user

    Returns:
        str: Completely hashed password
'''
def hash_password(username, password, salt) -> str:
    combined_input = f"{username}:{password}"
    peppersmsg = f"{'NEA2024'}:{username}"
    pepperkey= "Szymon4395"
    pepper = hmac.new(pepperkey.encode("UTF-8"),peppersmsg.encode("UTF-8"), hashlib.sha256).hexdigest()
    hashed_input = hmac.new(pepper.encode("UTF-8"),combined_input.encode("UTF-8"), hashlib.sha256).hexdigest()
    hashed_password = bcrypt.hashpw(hashed_input.encode("UTF-8"),salt)
    hashed_password = hashed_password + pepper.encode("UTF-8")
    return hashed_password.decode("UTF-8")

'''
    Creates a user account within the database storing their username, hashed password, salt
    
    Returns:
        bool: True if the user account is created successfully
'''
def create_User(user_name,password):
    if not SQLQueries.checkuser(user_name):
        salt = bcrypt.gensalt()
        Hashpassword = hash_password(user_name,password,salt)
        SQLQuery = "INSERT INTO Users (username, password,Salt) VALUES(?,?,?)"
        parameters = (user_name, Hashpassword, salt)
        msg = SQLQueries.AccountSQLExecutor(SQLQuery, parameters, "Create")
        return True            
    else:
        return False

'''
    Logs in user verifying the entered password against the stored hashed password

    Returns:
        str: "Login" if logged in successfully, "Wrong" if incorrect password is entered, "Zero" if the account doesn't exist
'''
def Login(user_name,password):
    if SQLQueries.checkuser(user_name):
        SQLQuery = "SELECT password,Salt FROM Users WHERE username = ?"
        parameters = (user_name,)
        hashedpassword, salt = SQLQueries.AccountSQLExecutor(SQLQuery, parameters, "Login")
        hashpass = hash_password(user_name,password, salt)
        if hashpass == hashedpassword:
            config_user.set_username(user_name)
            return "Login"
        else:
            return "Wrong"
    else:
        notificationhandler.trigger_notification("The account doesn't exist,\n maybe try creating an account?",1,"info")
        return "Zero"
            
'''
    Checks the strength of a given password giving it a score based on the criteria:
        Length greater than 8,
        Contains uppercase and lowercase characters,
        Contains numbers,
        Contains special characters
    Based on this score, it assigns a strength which it returns
'''
def password_strength(password):
    score = 0
    rating = ""

    if len(password) >= 8:
        score += 1
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 0:
        rating = "Very Weak"
    elif score == 1:
        rating = "Weak"
    elif score == 2:
        rating = "Moderate"
    elif score == 3:
        rating = "Strong"
    elif score == 4:
        rating = "Very Strong"
    return score, rating