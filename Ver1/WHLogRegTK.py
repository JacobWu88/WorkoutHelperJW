import tkinter as tk
import WHConfig as cf
class WorkoutHelperApp:
    def register(self):
        # Enter username and password
        try:
            # Read the file
            with open("users.txt", "r") as file:
                # count existing lines to find the next ID
                # "_" is used to show that the variable is needed but not for its value
                next_id = sum(1 for _ in file) + 1
        except FileNotFoundError:
            # If the file doesn't exist or empty, start at ID 1
            next_id = 1
        while True:
            username_label = tk.Label(self.root, text="Username: ")
            username_label.grid(row=0, column=0, pady=10)

            username = tk.Entry(self.root, width=20)
            username.grid(row=0, column=2, pady=10)
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


    def login(self):
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
    def login_or_register(self):
        # User can log in or register
        logreg_label = tk.Label(self.root, text="Workout Helper")
        logreg_label.grid(row=1, column=0, pady=10)
        # Login
        login = tk.Button(self.root, text="Login", width=10, command=self.login )
        login.grid(row=2, column=0, pady=10)
        # logged, user_id = self.login()
        # Register
        register = tk.Button(self.root, text="Register", width=10, command=self.register )
        register.grid(row=3, column=0, pady=10)
        # Exit
        leave = tk.Button(self.root, text="Exit", width=10, command=self.root.destroy)
        leave.grid(row=4, column=0, pady=10)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Workout Helper")
        self.root.geometry("300x200")
        self.login_or_register()

if __name__ == "__main__":
    app = WorkoutHelperApp()
    app.root.mainloop()