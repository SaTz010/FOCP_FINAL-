import getpass
from utility import *


PASSWORD_FILE = "passwd.txt"
current_user = None

def del_user():
    username_to_delete = input("Username: ").lower()
    
    passwords = load_passwords()
    filtered_passwords = [user for user in passwords if user[0] != username_to_delete]
    
    if len(passwords) == len(filtered_passwords):
        print("User not found. Nothing changed.")
    else:
        save_passwords(filtered_passwords)
        print("User Deleted.")

if __name__ == "__main__" :
    del_user()