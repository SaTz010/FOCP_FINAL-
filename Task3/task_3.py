# password_manager.py

import getpass
from utility import *
from add_user import *
from del_user import *
from passwd import *

PASSWORD_FILE = "passwd.txt"
current_user = None

def login():
    global current_user
    
    username = input("User: ").lower()
    password = getpass.getpass("Password: ")  # Masked input
    
    passwords = load_passwords()
    
    if any(user[0] == username and user[2] == password[::-1] for user in passwords):
        current_user = username
        print(current_user)
        print("Access granted.")
    else:
        print("Access denied.")

def display_current_user():
    global current_user
    
    if current_user is None:
        print("No user logged in.")
    else:
        print("Current User:", current_user)  # Display real name

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("-" * 30 )
        print("1. Create Account")
        print("2. Log In")
        print("3. Display Current User")
        print("4. Delete User")
        print("5. Change Password")
        print("6. Exit")
        print("-"* 30 )
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_user()
        elif choice == '2':
            login()
        elif choice == '3':
            display_current_user()
        elif choice == '4':
            del_user()
        elif choice == '5':
            passwd(current_user)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
