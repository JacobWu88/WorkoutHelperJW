"""
This Section is where the miscellaneous things happen like defining the rate of speed, menus, and small functions.
"""
# Menus
menu = ["Workout", "Previous Workouts", "Contact Us", "Log Out"]
workout_menu = ["WALK", "RUN", "BIKE", "BASKETBALL", "SKATING", "GYM", "BADMINTON", "SWIMMING", "HIKE",]
# Print Menus
def print_menu(menus):
    # Create a new list with the numbered menu
    numbered_menu = [f"{i+1}.{menu}" for i, menu in enumerate(menus)]
    line = "-" * len(" | ".join(numbered_menu))
    print(line)
    print(" | ".join(numbered_menu))
    print(line)

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
# If the user enters a number, convert it to the workout
number_to_workout = {"1": "WALK",
                    "2": "RUN",
                    "3": "BIKE",
                    "4": "BASKETBALL",
                    "5": "SKATING",
                    "6": "GYM",
                    "7": "BADMINTON",
                     "8": "SWIMMING",
                     "9": "HIKE"}



if __name__ == "__main__":
    print_menu(workout_menu)