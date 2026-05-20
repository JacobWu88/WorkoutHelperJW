import WHLogReg1 as lg

# Menus
menu = ["Workout", "Summary", "Previous Workouts", "Milestones", "Profile", "Contact Us", "Log Out"]
workout_menu = ["Walk", "Run", "Bike", "Basketball", "Skating", "Badminton"]
previous_workouts_menu = ["Date", "Workout", "Time"]
# Print Menus
def print_menu(menus):
    line = "-" * len(" | ".join(menus))
    print(line)
    print("|".join(menus))
    print(line)



if __name__ == "__main__":
    pass