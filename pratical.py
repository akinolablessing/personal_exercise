import re

import bcrypt



# username = input("Enter your username: ")
# password = input("Enter your password: ")
USER_DETAILS = 'user_details.txt'

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_to_file(username, hashed_password):
    with open(USER_DETAILS, 'a') as file:
        file.write(f"{username}:{hashed_password.decode('utf-8')}\n")


def register_user():
    while True:
        username = input("Enter your username: ")
        if not username:
            print("Username cannot be empty")
            continue
        break
    while True:
        password = input("Enter your password: ")
        if not password:
            print("Password cannot be empty")
            continue
        break

    save_to_file(username, hash_password(password))
try:
    def validate_username(username, password):
        with open(USER_DETAILS, 'r') as file:
            for line in file:
                stored_username,stored_password = line.strip().split(":")
                print(stored_username)
                if username == stored_username:
                    return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
except FileNotFoundError:
    print("File not found.")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if validate_username(username,password):
        print("Login successful")
    else:
        print("Login failed")



def main():
    menu= """"
    1. to register a new user
    2. to register another user
    3.to exit the program 
    >>>>>>"""

    choice = input(menu)


    match choice:
        case "1":
            register_user()
        case "2":
            login_user()
        case "3":
            print("Thank you for registering")
# main()


password = input("Enter your password: ")
while not re.fullmatch(r'\w{8,}',password):
    password = input("Enter your password: ")

# help(re.match)

