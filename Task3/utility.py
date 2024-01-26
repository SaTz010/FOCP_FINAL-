PASSWORD_FILE = "passwd.txt"

def load_passwords():
    with open(PASSWORD_FILE, "a+") as file:
        file.seek(0)
        lines = file.readlines()
    return [line.strip().split(":") for line in lines]

def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        for user in passwords:
            file.write(":".join(user) + "\n")