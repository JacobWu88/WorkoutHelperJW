import tkinter as tk
import WHConfig as cf
class WorkoutHelperApp:

    # Intro
    def login_or_register(self):
        # User can log in or register
        logreg_label = tk.Label(self.root, text="Workout Helper")
        logreg_label.grid(row=1, column=0, pady=10)
        # Login
        login = tk.Button(self.root, text="Login", width=10, )
        login.grid(row=2, column=0, pady=10)
        # logged, user_id = self.login()
        # Register
        register = tk.Button(self.root, text="Register", width=10, )
        register.grid(row=3, column=0, pady=10)
        # Exit
        leave = tk.Button(self.root, text="Exit", width=10, command=self.root.destroy)
        leave.grid(row=4, column=0, pady=10)

    def __init__(self):
        self.root = cf.create_window()
        self.root.title("Workout Helper")
        self.root.geometry("300x200")
        self.login_or_register()

if __name__ == "__main__":
    app = WorkoutHelperApp()
    app.root.mainloop()