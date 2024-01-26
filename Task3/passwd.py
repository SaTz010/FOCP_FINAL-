

import getpass
from utility import *

PASSWORD_FILE = "passwd.txt"

def login():
    global current_user
    
    username = input("User: ").lower()
    password = getpass.getpass("Password: ")  # Masked input
    
    passwords = load_passwords()
    
    if any(user[0] == username and user[2] == password[::-1] for user in passwords):
        current_user = username
        print(current_user)
        print("Access granted.")
        return current_user
    else:
        print("Access denied.")
        return False 
    
def passwd(current_user):
    print(current_user)
    
    if current_user is None:
        print("No user logged in. Please log in first.")
        return
    
    username = current_user
    current_password = getpass.getpass("Current Password: ")  # Masked input
    
    passwords = load_passwords()
    user_index = next((i for i, user in enumerate(passwords) if user[0] == username), None)
    
    if user_index is None or passwords[user_index][2] != current_password[::-1]:
        print("Invalid username or password. No change made.")
        return
    
    new_password = getpass.getpass("New Password: ")  # Masked input
    confirm_password = getpass.getpass("Confirm: ")  # Masked input
    
    if new_password == confirm_password:
        passwords[user_index][2] = new_password[::-1]  # Update password
        save_passwords(passwords)
        print("Password changed.")
    else:
        print("Passwords do not match. No change made.")


if __name__=="__main__" :
    if current_user := login(): #walrus operator 
        passwd(current_user)