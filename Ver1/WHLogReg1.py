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
    username = input("username: ")
    password = input("Password: ")
    # Write username and password to a file
    with open("users.txt", "a") as file:
        # ID for future reference
        file.write(f"{next_id} {username} {password}\n")
    print("Account Created!")

def login():
    username_input = input("Username: ")
    password_input = input("Password: ")
    with open("users.txt", "r") as file:
        users = file.readlines()
        match = False
        # Defines each user into each row
    for user in users:
        user_data = user.split()
        # Check if said username and password exists in the file
        if user_data[1] == username_input and user_data[2] == password_input:
            print("Login Successful!")
            print("Welcome, " + username_input + "!")
            return True
    if not match:
        print("Your username or Password is incorrect!")
    return False


# Intro
def login_or_register():
    logged = False
    # User can log in or register
    while not logged:
        logreg = input("Please Log in or Register, (or exit): ").replace(" ", "").lower()
        if logreg == "register":
            register()
        elif logreg == "login":
            logged = login()
        elif logreg == "exit":
            exit()
        # This won't be needed in gui
        else:
            print("Invalid Input!")
    return logged