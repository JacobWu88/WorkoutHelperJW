"""
This is the main script where the central logic happens.
"""
import WHConfig as cf
import WHWorkout as wk
import WHPreviousWorkouts as pw
import WHContactUs as cu
from WHLockHomeScreen import LockHome
from WHLogReg import LogReg
import tkinter as tk

class WorkoutHelperApp:
    def __init__(self):
        self.root = cf.create_window()
        self.user_id = None

        self.lhs = LockHome(self.root)
        self.lg = LogReg(self.root, self.on_user_logged)
        # Lock Screen
        self.show_lock_screen()
        # Centre (almost) everything horizontally
        self.root.columnconfigure(0, weight=1)


    def show_lock_screen(self):
        self.lhs.show_lock_screen()

        continue_button = tk.Button(self.root, text="Continue", command=self.show_login_screen)
        continue_button.grid(row=2, column=0, pady=10)

    def show_login_screen(self):
        self.lg.login_or_register()
    # Define user ID
    def on_user_logged(self, user_id):
        self.user_id = user_id
        cf.clear_screen(self.root)
        self.show_main_menu()
    # Go to the main menu
    def show_main_menu(self):
        main_menu = tk.Frame(self.root)
        main_menu.grid(row=0, column=0, pady=10, sticky="nsew")
        cf.create_menu(main_menu,cf.menu, self.on_menu_item_click)


    def on_menu_item_click(self, item_selected):
        # Menu items to actual pages
        if item_selected == "Workout":
            cf.clear_screen(self.root)
            wk.WorkoutTimer(self.root, self.user_id, self.show_main_menu)

        elif item_selected == "Previous Workouts":
            cf.clear_screen(self.root)
            pw.PreviousWorkouts(self.root, self.user_id, self.show_main_menu)

        elif item_selected == "Contact Us":
            cf.clear_screen(self.root)
            cu.ContactUs(self.root, self.show_main_menu)

        elif item_selected == "Log Out":
            self.user_id = None
            cf.clear_screen(self.root)
            self.show_lock_screen()

if __name__ == "__main__":
    app = WorkoutHelperApp()
    app.root.mainloop()

