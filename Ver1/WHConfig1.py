import WHLogReg1 as lg

# Menus
menu = ["Workout", "Previous Workouts", "Contact Us", "Log Out"]
workout_menu = ["Walk", "Run", "Bike", "Basketball", "Skating", "Badminton"]
# Print Menus
def print_menu(menus):
    line = "-" * len(" | ".join(menus))
    print(line)
    print(" | ".join(menus))
    print(line)



if __name__ == "__main__":
    print_menu(workout_menu)