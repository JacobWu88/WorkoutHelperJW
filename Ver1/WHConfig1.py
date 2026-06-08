"""
This Section is where the miscellaneous things happen like defining the rate of speed, menus, and small functions.
"""
# Menus
menu = ["Workout", "Previous Workouts", "Contact Us", "Log Out"]
workout_menu = ["WALK", "RUN", "BIKE", "BASKETBALL", "SKATING", "GYM", "BADMINTON"]
# Print Menus
def print_menu(menus):
    line = "-" * len(" | ".join(menus))
    print(line)
    print(" | ".join(menus))
    print(line)

# Which workout fits into which unit of measurement
kilometres = ["WALK", "RUN", "BIKE"]
kilojoules = ["HIGH JUMP", "GYM", "BADMINTON", "BASKETBALL", "SKATING"]

# The convert rate for time * multiplier for each workout
converters = {"WALK": 1.39,
              "RUN": 2.78,
              "BIKE": 6.94,
              "BASKETBALL": 0.75,
              "SKATING": 20,
              "HIGH JUMP": 0.5,
              "GYM": 31,
              "BADMINTON": 3
              }

if __name__ == "__main__":
    print_menu(workout_menu)