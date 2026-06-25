"""
This is the main script where the central logic happens.
"""
import WHConfig as cf
import WHLogRegTK as lg
import WHLockHomeScreen as lhs
import WHWorkout as wk
import WHPreviousWorkouts as pw
import WHContactUs as cu
from WHLockHomeScreen import LockHome
from WHLogRegTK import LogReg
import tkinter as tk

class WorkoutHelperApp:
    def __init__(self):
        self.root = cf.create_window()
        self.user_id = None

        self.lhs = LockHome(self.root)
        self.lg = LogReg(self.root, self.on_user_logged)
        # Lock Screen
        self.show_lock_screen()
    def show_lock_screen(self):
        self.lhs.show_lock_screen()

        continue_button = tk.Button(self.root, text="Continue", command=self.show_login_screen)
        continue_button.grid(row=2, column=0, pady=10)

    def show_login_screen(self):
        self.lg.login_or_register()

    def on_user_logged(self, user_id):
        self.user_id = user_id
        print(f"User logged in: {user_id}")
        cf.clear_screen(self.root)
        self.show_main_menu()

    def show_main_menu(self):
        main_menu = tk.Frame(self.root)
        main_menu.grid(row=0, column=0, pady=10)
        cf.create_menu(main_menu,cf.menu, self.on_menu_item_click)


    def on_menu_item_click(self, item_selected):
        if item_selected == "Workout":
            wk.Workout(self.root, self.user_id)
        elif item_selected == "Previous Workouts":
            pw.PreviousWorkouts(self.root, self.user_id)
        elif item_selected == "Contact Us":
            cu.ContactUs(self.root)
        elif item_selected == "Log Out":
            print("Logging out...")
            self.user_id = None
            self.show_lock_screen()
        else:
            print("Invalid menu item selected.")


if __name__ == "__main__":
    app = WorkoutHelperApp()
    app.root.mainloop()

