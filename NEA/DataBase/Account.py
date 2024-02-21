import bcrypt
import hashlib
import hmac
import re
from DataBase import config, SQLQueries

config_user = config.Config()

#Hashes the user password using their username and salt, then stores it within the database
def hash_password(username, password, salt) -> str:
    # Combine username and password to hash it with the pepper
    combined_input = f"{username}:{password}"
    #Creates the pepper which will be added to the end of the hashed password to make it harder to perform rainbow table attacks 
    peppersmsg = f"{'NEA2024'}:{username}"
    pepperkey= "Szymon4395"
    pepper = hmac.new(pepperkey.encode("UTF-8"),peppersmsg.encode("UTF-8"), hashlib.sha256).hexdigest()
    hashed_input = hmac.new(pepper.encode("UTF-8"),combined_input.encode("UTF-8"), hashlib.sha256).hexdigest()
    # Hashes the password 
    hashed_password = bcrypt.hashpw(hashed_input.encode("UTF-8"),salt)
    hashed_password = hashed_password + pepper.encode("UTF-8")
    return hashed_password.decode("UTF-8")

#Creates the user account within the database storing their username, hashed password, salt
def create_User(user_name,password):
    if not SQLQueries.checkuser(user_name):
        #Generates a unique salt that will be added to the hashed password
        salt = bcrypt.gensalt()
        Hashpassword = hash_password(user_name,password,salt)
        SQLQuery = "INSERT INTO Users (username, password,Salt) VALUES(?,?,?)"
        parameters = (user_name, Hashpassword, salt)
        msg = SQLQueries.AccountSQLExecutor(SQLQuery, parameters, "Create")
        print(msg)
                        
    else:
        print("The Username is taken")

def Login(user_name,password):
    if SQLQueries.checkuser(user_name):
        SQLQuery = "SELECT password,Salt FROM Users WHERE username = ?"
        parameters = (user_name,)
        hashedpassword, salt = SQLQueries.AccountSQLExecutor(SQLQuery, parameters, "Login")
        hashpass = hash_password(user_name,password, salt)
        if hashpass == hashedpassword:
            config_user.set_username(user_name)
            print(user_name)
            return f"Logged In Successfully as {user_name}"
        else:
            return "Incorrect Password"
            
         
    else:
        return "The username doesn't exist, maybe try creating an account?"
            
def password_strength(password):
    # Initialize score and rating
    score = 0
    rating = ""

    # Check for length
    if len(password) >= 8:
        score += 1

    # Check for uppercase and lowercase letters
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1

    # Check for numbers
    if re.search("[0-9]", password):
        score += 1

    # Check for special characters
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Assign rating based on score
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