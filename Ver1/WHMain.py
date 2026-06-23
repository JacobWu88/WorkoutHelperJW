"""
This is the main script where the central logic happens.
"""
import WHConfig as cf
import WHLogRegTK as lg
import WHLockHomeScreen as lhs
import WHWorkout as wk
import WHPreviousWorkouts as pw
import WHContactUs as cu
import tkinter as tk

class WorkoutHelperApp:
    def __init__(self):
        self.root = cf.create_window()
        self.user_id = None

        self.lock_home = lhs
        self.log_reg = lg
        # Lock Screen
        self.show_lock_screen()

    def show_lock_screen(self):
        cf.clear_screen(self.root)
        lhs.WorkoutHelperApp()

        continue_button = tk.Button(self.root, text="Continue", command=lambda: self.log_reg.WorkoutHelperApp())
        continue_button.grid(row=1, column=0, pady=10)


if __name__ == "__main__":
    app = WorkoutHelperApp()
    app.root.mainloop()

