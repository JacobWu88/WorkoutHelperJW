"""
This Section shows Previous Workouts in the format of Date | Workout | Time
"""

import WHConfig as cf
import tkinter as tk
from tkinter import ttk, messagebox

class PreviousWorkouts:
    def __init__(self, root, user_id, on_back_callback=None):
        self.root = root
        self.user_id = user_id
        self.on_back_callback = on_back_callback
        self.tree = None
        self.setup_ui()

    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Title
        tk.Label(main_frame, text="Previous Workouts", font=("Arial", 24, "bold")).pack(pady=10)

        # Treeview for workouts
        columns = ("No.", "Date", "Workout", "Time", "m/kj")
        self.tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=15)

        # Define headings
        self.tree.heading("No.", text="No.")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Workout", text="Workout")
        self.tree.heading("Time", text="Time")
        self.tree.heading("m/kj", text="m/kj")

        # Define column widths
        self.tree.column("No.", width=50, anchor="center")
        self.tree.column("Date", width=100, anchor="center")
        self.tree.column("Workout", width=120, anchor="center")
        self.tree.column("Time", width=80, anchor="center")
        self.tree.column("m/kj", width=80, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Load workouts
        self.load_workouts()

        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # View lap times button
        tk.Button(button_frame, text="View Lap Times", font=("Arial", 12),
                  bg="#2196F3", fg="white", command=self.view_lap_times).pack(side="left", padx=5)

        # Back button
        tk.Button(button_frame, text="Back", font=("Arial", 12),
                  command=self.go_back).pack(side="left", padx=5)

    def load_workouts(self):
        try:
            with open("workout_history.txt", "r") as file:
                lines = file.readlines()
                user_workouts = [line for line in lines if line.startswith(str(self.user_id))]

                if not user_workouts:
                    messagebox.showinfo("No Workouts", "You have no previous workouts!")
                    return

                for workout in user_workouts:
                    workouts = workout.split()
                    # workouts format: [user_id, workout_id, workout_name, special_value, date, time]
                    self.tree.insert("", "end", values=(
                        workouts[1],  # No.
                        workouts[4],  # Date
                        workouts[2],  # Workout
                        workouts[5],  # Time
                        workouts[3]   # m/kj
                    ))

        except FileNotFoundError:
            messagebox.showinfo("No Workouts", "You have no previous workouts!")

    def view_lap_times(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a workout to view lap times!")
            return

        # Get the workout ID from the selected row
        workout_id = self.tree.item(selected_item[0])["values"][0]

        try:
            with open("lap.txt", "r") as file:
                found = False
                for lap in file:
                    if lap.strip().startswith(str(workout_id)):
                        lap_parts = lap.split()
                        # Check if this workout belongs to the user
                        if str(self.user_id) == lap_parts[1]:
                            found = True
                            self.show_lap_window(lap_parts)
                            break
                        else:
                            messagebox.showerror("Permission Denied",
                                               "You don't have permission to view this workout.")
                            return

                if not found:
                    messagebox.showinfo("No Lap Data", "No lap times found for this workout.")

        except FileNotFoundError:
            messagebox.showinfo("No Lap Data", "No lap data file found.")

    def show_lap_window(self, lap_parts):
        # Create a new window for lap times
        lap_window = tk.Toplevel(self.root)
        lap_window.title("Lap Times")
        lap_window.geometry("400x400")

        tk.Label(lap_window, text="Lap Times", font=("Arial", 18, "bold")).pack(pady=10)

        # Create treeview for laps
        columns = ("Unit", "Time")
        lap_tree = ttk.Treeview(lap_window, columns=columns, show="headings", height=12)

        lap_tree.heading("Unit", text="Unit")
        lap_tree.heading("Time", text="Time")

        lap_tree.column("Unit", width=150, anchor="center")
        lap_tree.column("Time", width=150, anchor="center")

        lap_tree.pack(padx=20, pady=10, fill="both", expand=True)

        # Parse lap data (skip first 3 parts: workout_id, user_id, workout_name)
        lap_data = lap_parts[3:]
        lap_it = iter(lap_data)
        lap_pairs = list(zip(lap_it, lap_it))

        for pair in lap_pairs:
            lap_tree.insert("", "end", values=(pair[0], pair[1]))

        # Close button
        tk.Button(lap_window, text="Close", font=("Arial", 12),
                  command=lap_window.destroy).pack(pady=10)

    def go_back(self):
        cf.clear_screen(self.root)
        if self.on_back_callback:
            self.on_back_callback()


# Testing
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Workout Helper")
    root.geometry("600x600")
    app = PreviousWorkouts(root, 9999)
    root.mainloop()