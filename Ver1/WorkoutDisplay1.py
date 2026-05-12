def register():
    #enter username and password
    try:
        #read the file
        with open("users.txt", "r") as file:
            #count existing lines to find the next ID
            #"_" is used to show that the variable is needed but not for its value
            next_id = sum(1 for _ in file) + 1
    except FileNotFoundError:
        #if the file doesn't exist or empty, start at ID 1
        next_id = 1
    username = input("username: ")
    password = input("Password: ")
    #write username and password to a file
    with open("users.txt", "a") as file:
        file.write(f"{next_id} {username} {password}\n")
    print("Account Created!")

def login():
    username_input = input("Username: ")
    password_input = input("Password: ")
    with open("users.txt", "r") as file:
        users = file.readlines()
        #defines each user into each row
    for user in users:
        user_data = user.split()
        #check if said username and password exists in the file
        if user_data[0] == username_input and user_data[1] == password_input:
            print("Login Successful!")
        else:
            print("Your username or Password is incorrect!")
            return
#intro
print("Welcome!")
print("This is te Workout Helper, for all your workout needs!")
#User can login or register
logreg = input("Please Login or Register: ").lower()
if logreg == "register":
    register()
elif logreg == "login":
    login()

