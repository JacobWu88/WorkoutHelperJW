import tkinter as tk
import WHConfig as cf
from Ver1.WHConfig import clear_screen


class WorkoutHelperApp:
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
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
        for widget in self.root.winfo_children():
            widget.destroy()
        title_label = tk.Label(self.root, text="LOGIN", font=("Arial", 24))
        title_label.grid(row=0, column=2, pady=20)
        username_label = tk.Label(self.root, text="Username: ")
        username_label.grid(row=1, column=0, pady=10)
        password_label = tk.Label(self.root, text="Password: ")
        password_label.grid(row=2, column=0, pady=10)
        username_input = tk.Entry(self.root, width=20)
        username_input.grid(row=1, column=2, pady=10)
        password_input = tk.Entry(self.root, width=20, show="*")
        password_input.grid(row=2, column=2, pady=10)
        login_button = tk.Button(self.root, text="Login", command=lambda:self.verify(username_input.get(), password_input.get()))
        login_button.grid(row=3, column=2, pady=10)

    def verify(self, username_input, password_input):
        try:
            with open("users.txt", "r") as file:
                users = file.readlines()
        except FileNotFoundError:
            error_label = tk.Label(self.root, text="Password or Username is incorrect!")
            error_label.grid(row=4, column=2, pady=10)
            self.root.after(2000, error_label.destroy)
            return False, None

        for user in users:
            user_data = user.split()
            # Check if said username and password exists in the file
            if user_data[1] == username_input and user_data[2] == password_input:
                logged_in_label = tk.Label(self.root, text=f"Welcome, {user_data[1]}!")
                logged_in_label.grid(row=4, column=2, pady=10)
                self.root.after(1000, self.clear_window)
                # Get and return the user_id
                user_id = user_data[0]
                return True, user_id

        error_label = tk.Label(self.root, text="Password or Username is incorrect!")
        error_label.grid(row=4, column=2, pady=10)
        self.root.after(2000, error_label.destroy)
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
        self.root = cf.create_window()
        self.login_or_register()


if __name__ == "__main__":
    app = WorkoutHelperApp()
    app.root.mainloop()