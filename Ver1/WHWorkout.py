import tkinter as tk
from tkinter import messagebox
import time
import WHConfig as cf


def get_next_workout_id():
    try:
        with open("workout_history.txt", "r") as file:
            return sum(1 for _ in file) + 1
    except FileNotFoundError:
        return 1


class WorkoutTimer:
    # Define everything
    def __init__(self, root, user_id, on_back_callback=None):
        self.root = root
        self.user_id = user_id
        self.on_back_callback = on_back_callback
        self.workout_name = None
        self.start_time = None
        self.running = False
        self.lap_data = []
        self.multiplier = 1
        self.special = ""
        self.workout_id = get_next_workout_id()
        self.workout_var = tk.StringVar()

        self.start_btn = None
        self.timer_label = None
        self.lap_btn = None
        self.stop_btn = None
        self.lap_listbox = None

        self.setup_ui()

    # Convert time to a special unit
    def convert(self, timing):
        return timing * self.multiplier

    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=20, pady=20)

        # Title
        tk.Label(main_frame, text="Workout Timer", font=("Arial", 24, "bold")).pack(pady=10)

        # Workout selection
        tk.Label(main_frame, text="Select Workout:", font=("Arial", 14)).pack(pady=5)

        workout_dropdown = tk.OptionMenu(main_frame, self.workout_var, *cf.workout_menu)
        workout_dropdown.config(width=20, font=("Arial", 12))
        workout_dropdown.pack(pady=5)

        # Start button
        self.start_btn = tk.Button(main_frame, text="Start Workout", font=("Arial", 14),
                                   bg="#4CAF50", command=self.start_workout)
        self.start_btn.pack(pady=10)

        # Timer display
        self.timer_label = tk.Label(main_frame, text="00:00.00", font=("Arial", 48, "bold"))
        self.timer_label.pack(pady=20)

        # Lap button
        self.lap_btn = tk.Button(main_frame, text="Lap", font=("Arial", 14),
                                 bg="#2196F3", command=self.record_lap, state="disabled")
        self.lap_btn.pack(pady=5)

        # Stop button
        self.stop_btn = tk.Button(main_frame, text="Stop Workout", font=("Arial", 14),
                                  bg="#f44336", command=self.stop_workout, state="disabled")
        self.stop_btn.pack(pady=5)

        # Lap display
        tk.Label(main_frame, text="Laps:", font=("Arial", 12, "bold")).pack(pady=(10, 5))

        lap_frame = tk.Frame(main_frame)
        lap_frame.pack(fill="both", expand=True)
        # If lap scrollbar is needed
        scrollbar = tk.Scrollbar(lap_frame)
        scrollbar.pack(side="right", fill="y")

        self.lap_listbox = tk.Listbox(lap_frame, font=("Arial", 10),
                                      yscrollcommand=scrollbar.set, height=8, width=40)
        self.lap_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.lap_listbox.yview)

        # Back button
        tk.Button(main_frame, text="Back", font=("Arial", 12),
                  command=self.go_back).pack(pady=10)

    def start_workout(self):
        self.workout_name = self.workout_var.get()
        # Check if the workout is valid
        if not self.workout_name or self.workout_name not in cf.workout_menu:
            messagebox.showerror("Error", "Please select a valid workout!")
            return

        # Set unit and multiplier
        if self.workout_name in cf.kilometres:
            self.special = "m"
        elif self.workout_name in cf.kilojoules:
            self.special = "Kj"

        self.multiplier = cf.converters.get(self.workout_name, 1)

        # Countdown
        self.countdown(3)

    def countdown(self, count):
        if count > 0:
            self.timer_label.config(text=str(count))
            self.root.after(500, lambda: self.countdown(count - 1))
        else:
            self.timer_label.config(text="GO!")
            self.root.after(500, self.begin_workout)

    def begin_workout(self):
        self.running = True
        self.start_time = time.time()
        self.lap_data = []
        self.lap_listbox.delete(0, tk.END)

        # Update button states
        self.start_btn.config(state="disabled")
        self.lap_btn.config(state="normal")
        self.stop_btn.config(state="normal")

        self.update_timer()

    def update_timer(self):
        if self.running:
            elapsed = time.time() - self.start_time
            minutes = int(elapsed // 60)
            seconds = elapsed % 60
            self.timer_label.config(text=f"{minutes:02d}:{seconds:05.2f}")
            self.root.after(10, self.update_timer)

    def record_lap(self):
        if self.running:
            lap_time = round(time.time() - self.start_time, 2)
            special_value = round(self.convert(lap_time), 2)

            lap_number = len(self.lap_data) + 1
            lap_text = f"Lap {lap_number}: {lap_time}s ({special_value}{self.special})"

            self.lap_listbox.insert(tk.END, lap_text)
            self.lap_data.append(f"{special_value}{self.special} {lap_time}s")

    def stop_workout(self):
        if not self.running:
            return

        self.running = False
        end_time = time.time()
        total_time = round(end_time - self.start_time, 2)
        special_value = round(self.convert(total_time), 2)

        # Update button states
        self.start_btn.config(state="normal")
        self.lap_btn.config(state="disabled")
        self.stop_btn.config(state="disabled")

        # Show results
        messagebox.showinfo("Workout Complete",
                            f"Your {self.workout_name} workout took {total_time} seconds\n"
                            f"{special_value}{self.special}")

        # Save workout
        self.save_workout(total_time, special_value)

        # Reset timer
        self.timer_label.config(text="00:00.00")

    def save_workout(self, total_time, special_value):
        # Save to workout_history.txt
        with open("workout_history.txt", "a") as file:
            file.write(f"{self.user_id} {self.workout_id} {self.workout_name} "
                       f"{special_value}{self.special} {time.strftime('%d/%m/%Y')} {total_time}\n")

        # Save to lap.txt
        with open("lap.txt", "a") as f:
            if self.lap_data:
                f.write(f"\n{self.workout_id} {self.user_id} {self.workout_name} {' '.join(self.lap_data)}")
            else:
                f.write(f"\n{self.workout_id} {self.user_id} {self.workout_name} "
                        f"{special_value}{self.special} {total_time}s")

        # Workout ID for next workout
        self.workout_id += 1

    # Go back to the main menu
    def go_back(self):
        # if workout is running
        if self.running:
            if messagebox.askyesno("Warning", "Workout in progress. Are you sure you want to go back?"):
                self.running = False
                cf.clear_screen(self.root)
                if self.on_back_callback:
                    self.on_back_callback()
        # If workout isn't running
        else:
            cf.clear_screen(self.root)
            if self.on_back_callback:
                self.on_back_callback()


# Main window setup for testing
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Workout Helper")
    app = WorkoutTimer(root, 9999)
    root.mainloop()
