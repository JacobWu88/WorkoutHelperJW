import WHConfig as cf

def register():
    # Enter username and password
    try:
        # Read the file
        with open("users.txt", "r") as file:
            #count existing lines to find the next ID
            #"_" is used to show that the variable is needed but not for its value
            next_id = sum(1 for _ in file) + 1
    except FileNotFoundError:
        # If the file doesn't exist or empty, start at ID 1
        next_id = 1
    while True:
        username = input("username: ")
        try:
            with open("users.txt", "r") as file:
                users = file.readlines()
        except FileNotFoundError:
            users = []

        # Check if a username already exists
        username_exists = False
        for user in users:
            user_data = user.split()
            if user_data[1] == username:
                username_exists = True
                print("Username Already Exists!")
                break
        if not username_exists:
            break
    password = input("Password: ")
    # Write username and password to a file
    with open("users.txt", "a") as file:
        # ID for future reference
        file.write(f"{next_id} {username} {password}\n")
    print("Account Created!")
    return None


def login():
    username_input = input("Username: ")
    password_input = input("Password: ")
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
    except FileNotFoundError:
        print("No users found!")
        return False, None
    
    for user in users:
        user_data = user.split()
        # Check if said username and password exists in the file
        if user_data[1] == username_input and user_data[2] == password_input:
            print("Login Successful!")
            print(f"Welcome, {user_data[1]}!")
            # Get and return the user_id
            user_id = user_data[0]
            return True, user_id
    
    print("Your username or Password is incorrect!")
    return False, None


# Intro
def login_or_register():
    # User can log in or register
    while True:
        logreg = input("Please Log in (1) or Register (2) , or exit (3): ").lower()
        # Login
        if logreg in ("1", "login", "log in", "log"):
            logged, user_id = login()
            if logged:
                return True, user_id
        # Register
        elif logreg in ("2", "register", "reg"):
            register()
        # Exit
        elif logreg in ("3", "exit", "quit"):
            print("Exiting...")
            exit()
        else:
            print("Invalid Input!")
if __name__ == "__main__":
    login_or_register()