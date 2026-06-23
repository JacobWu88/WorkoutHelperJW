import tkinter as tk
import WHConfig as cf

class WorkoutHelperApp:
    def back(self):
        back_button = tk.Button(self.root, text="Back", width=10, command=self.login_or_register)
        back_button.grid(row=0, column=0, pady=10)

    def show_screen(self):
        # Enter username and password
        username_label = tk.Label(self.root, text="Username: ")
        username_label.grid(row=1, column=0, pady=10)
        password_label = tk.Label(self.root, text="Password: ")
        password_label.grid(row=2, column=0, pady=10)

        username_input = tk.Entry(self.root, width=20)
        username_input.grid(row=1, column=2, pady=10)
        password_input = tk.Entry(self.root, width=20, show="*")
        password_input.grid(row=2, column=2, pady=10)
        return username_input, password_input

    def register(self):
        cf.clear_screen(self.root)
        self.back()
        title_label = tk.Label(self.root, text="REGISTER", font=("Arial", 24))
        title_label.grid(row=0, column=2, pady=20)
        username, password  = self.show_screen()
        register_button = tk.Button(self.root, text="Register", command=lambda:self.register_check(username, password))
        register_button.grid(row=3, column=2, pady=10)


    def register_check(self, username, password):
        username = username.get()
        password = password.get()

        if not username or not password:
            error_label = tk.Label(self.root, text="Please fill in all fields!")
            error_label.grid(row=4, column=2, pady=10)
            self.root.after(2000, error_label.destroy)
            return False
        try:
            # Read the file
            with open("users.txt", "r") as file:
                # count existing lines to find the next ID
                # "_" is used to show that the variable is needed but not for its value
                next_id = sum(1 for _ in file) + 1
        except FileNotFoundError:
            # If the file doesn't exist or empty, start at ID 1
            next_id = 1
            users = []

            # Check if a username already exists
            username_exists = False
            for user in users:
                user_data = user.split()
                if len(user_data) >= 2:
                    if user_data[1] == username:
                        username_exists = True
                        break
            if username_exists:
                error_label = tk.Label(self.root, text="Username Already Exists!")
                error_label.grid(row=4, column=2, pady=10, wraplength=300)
                self.root.after(2000, error_label.destroy)
                return False
        # Write username and password to a file
        with open("users.txt", "a") as file:
            # ID for future reference
            file.write(f"{next_id} {username} {password}\n")
            registered_label = tk.Label(self.root, text="Account Created!")
            registered_label.grid(row=4, column=2, pady=10)
            self.root.after(1000, cf.clear_screen(self.root))
            return True


    def login(self):
        cf.clear_screen(self.root)
        self.back()
        title_label = tk.Label(self.root, text="LOGIN", font=("Arial", 24))
        title_label.grid(row=0, column=2, pady=20)
        username, password = self.show_screen()
        login_button = tk.Button(self.root, text="Login", command=lambda:self.verify(username, password))
        login_button.grid(row=3, column=2, pady=10)

    def verify(self, username_input, password_input):
        username_input = username_input.get()
        password_input = password_input.get()
        print(username_input, password_input)
        try:
            with open("users.txt", "r") as file:
                users = file.readlines()
        except FileNotFoundError:
            error_label = tk.Label(self.root, text="Password or Username is incorrect!", wraplength=200)
            error_label.grid(row=4, column=2)
            self.root.after(2000, error_label.destroy)
            return False, None

        for user in users:
            user_data = user.split()
            # Check if said username and password exists in the file
            try:
                if user_data[1] == username_input and user_data[2] == password_input:
                    logged_in_label = tk.Label(self.root, text=f"Welcome, {user_data[1]}!")
                    logged_in_label.grid(row=4, column=2, pady=10)
                    self.root.after(1000, cf.clear_screen(self.root))
                    # Get and return the user_id
                    user_id = user_data[0]
                    return True, user_id
            except IndexError:
                print("index")

        error_label = tk.Label(self.root, text="Password or Username is incorrect!", wraplength=200)
        error_label.grid(row=4, column=2)
        self.root.after(2000, error_label.destroy)
        return False, None

    # Intro
    def login_or_register(self):
        cf.clear_screen(self.root)
        # User can log in or register
        logreg_label = tk.Label(self.root, text="Workout Helper", font=("Arial", 24))
        logreg_label.grid(row=1, column=2, pady=10)
        # Login
        login = tk.Button(self.root, text="Login", width=10, command=self.login )
        login.grid(row=2, column=2, pady=10)
        # Register
        register = tk.Button(self.root, text="Register", width=10, command=self.register )
        register.grid(row=3, column=2, pady=10)
        # Exit
        leave = tk.Button(self.root, text="Exit", width=10, command=self.root.destroy)
        leave.grid(row=4, column=2, pady=10)

    def __init__(self):
        self.root = cf.create_window()
        self.login_or_register()


if __name__ == "__main__":
    app = WorkoutHelperApp()
    app.root.mainloop()