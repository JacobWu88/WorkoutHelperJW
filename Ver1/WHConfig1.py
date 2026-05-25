"""
This Section is where the miscellaneous things happen like defining the rate of speed, menus, and small functions.
"""
# Menus
menu = ["Workout", "Previous Workouts", "Contact Us", "Log Out"]
workout_menu = ["WALK", "RUN", "BIKE", "BASKETBALL", "SKATING", "BADMINTON"]
# Print Menus
def print_menu(menus):
    line = "-" * len(" | ".join(menus))
    print(line)
    print(" | ".join(menus))
    print(line)

kilometres = ["WALK", "RUN", "BIKE", "BASKETBALL"]
kilojoules = ["HIGH JUMP", "GYM"]


if __name__ == "__main__":
    print_menu(workout_menu)