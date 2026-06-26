import WHConfig as cf
import tkinter as tk
import time

class LockHome:

    def show_lock_screen(self):
        cf.clear_screen(self.root)
        welcome = tk.Label(self.root,
            text="Welcome!",
            font=("Arial", 24))
        welcome.grid(row=0, column=0, columnspan=2, pady=20)

        description = tk.Label(self.root,
            text="This is the Workout Helper,\nfor all your workout needs!",
            font=("Arial", 14))
        description.grid(row=1, column=0, columnspan=2)

    def show_home_screen(self):
        title_label = tk.Label(self.root, text="HOME", font=("Arial", 24))
        title_label.grid(row=0, column=0, pady=20)


        self.update_time()
    def update_time(self):
        current_date = time.strftime("%d/%m/%Y")
        current_time = time.strftime("%H:%M:%S")

        self.date_label.config(text=f"Date: {current_date}")
        self.time_label.config(text=f"Time: {current_time}")
        # Update every 1000ms (1 second)
        self.root.after(1000, self.update_time)

    def __init__(self, root):
        if __name__ == "__main__":
            self.root = cf.create_window()
            self.show_lock_screen()
        else:
            self.root = root
        self.date_label = tk.Label(self.root, font=("arial", 18, "bold"))
        self.date_label.grid(column=0, row=1)

        self.time_label = tk.Label(self.root, font=("arial", 18, "bold"))
        self.time_label.grid(column=0, row=2)


if __name__ == "__main__":
    root = cf.create_window()
    app = LockHome(root)
    app.root.mainloop()