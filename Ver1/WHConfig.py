"""
This Section is where the miscellaneous things happen like defining the rate of speed, menus, and small functions.
"""

import tkinter as tk

def create_window():
    root = tk.Tk()
    root.title("Workout Helper")
    root.geometry("400x600")
    return root
def clear_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

def create_menu(root, menu_items, callback):
    root.columnconfigure(2, weight=1)
    title_label = tk.Label(root, text="Workout Helper", font=("Arial", 24))
    title_label.grid(row=0, column=2, pady=20)
    for index, item in enumerate(menu_items):
        item_button = tk.Button(root, text=item, command=lambda menu_items=item: callback(menu_items))
        item_button.grid(row=index+1, column=2, pady=10)

# Menus
menu = ["Workout", "Previous Workouts", "Contact Us", "Log Out"]
workout_menu = ["WALK", "RUN", "BIKE", "BASKETBALL", "SKATING", "GYM", "BADMINTON", "SWIMMING", "HIKE",]
# Print Menus
#def print_menu(menus):


# Which workout fits into which unit of measurement
kilometres = ["WALK", "RUN", "BIKE", "HIKE"]
kilojoules = ["GYM", "BADMINTON", "BASKETBALL", "SKATING", "SWIMMING"]

# The convert rate for time * multiplier for each workout
converters = {"WALK": 1.39,
              "RUN": 2.78,
              "BIKE": 6.94,
              "BASKETBALL": 0.75,
              "SKATING": 20,
              "GYM": 31,
              "BADMINTON": 3,
              "SWIMMING": 1.39,
              "HIKE": 1.39
              }



if __name__ == "__main__":
    print("Please run 'WHMain.py' to use this program!")