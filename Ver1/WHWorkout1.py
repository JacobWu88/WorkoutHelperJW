"""
This section is for the workout.
"""

import time
import WHConfig1 as cf

def workout(user_id):
    # Convert the time to the correct unit
    def convert(timing):
        converted = timing * multiplier
        return converted

    workout_name = input("What workout do you want to do? ").upper()
    if workout_name in cf.workout_menu:
        # Define the unit of the workout
        if workout_name in cf.kilometres:
         special = "m"
        elif workout_name in cf.kilojoules:
         special = "Kj"
        else:
            print("Invalid Workout")
        # Get the multiplier for the workout
        multiplier = cf.converters.get(workout_name)
        # Give each workout a unique ID
        try:
            with open("workout_history.txt", "r") as file:
                # Count existing lines to find the next ID
                workout_id = sum(1 for _ in file) + 1
        except FileNotFoundError:
            # If the file doesn't exist or empty, start at ID 1
            workout_id = 1
            # Countdown
        print("3")
        time.sleep(0.5)
        print("2")
        time.sleep(0.5)
        print("1")
        time.sleep(0.5)
        print("GO!")
        # Start time is the current time
        start_time = time.time()
        choice = "go"
        lapped = False
        while choice != "stop":
            # Lap
            choice = input("Enter 'L' to lap or Press Enter to stop the workout. ").lower()
            if choice == "l":
                # Calculate the lap time
                lap_time = round(time.time() - start_time, 2)
                print(f"Lap time: {lap_time} seconds")
                special_value = round(convert(lap_time), 2)
                with open("lap.txt", "r") as f:
                    lined = f.readlines()
                with open("lap.txt", "a") as f:
                    # Write the workout ID, Name, value, unit, and laptime to the file
                    if len(lined) > 0:
                        f.write("\n")
                    f.write(f"{workout_id} {user_id} {workout_name} {special_value}{special} {lap_time}s")
                    lapped = True
                    while choice != "stop":
                        choice = input("Enter 'L' to lap or Press Enter to stop the workout. ").lower()
                        if choice == "l":
                            lap_time = round(time.time() - start_time, 2)
                            print(f"Lap time: {lap_time} seconds")
                            special_value = round(convert(lap_time), 2)
                            f.write(f" {special_value}{special} {lap_time}s")
                        elif choice == "":
                            print("Stopping Workout.")
                            choice = "stop"
            elif choice == "":
                print("Stopping Workout.")
                choice = "stop"
            else:
                print("Invalid")
        #  End time is the time the user stopped the workout
        end_time = time.time()
        # Calculate the total time
        total_time = round(end_time - start_time, 2)
        special_value = round(convert(total_time), 2)
        print(f"Your workout took {total_time} seconds, {special_value}{special}")
        # Write the workout to a file
        with open("workout_history.txt", "a") as file:
            file.write(f"{user_id} {workout_id} {workout_name} {special_value}{special} {time.strftime("%d/%m/%Y")} {total_time}    \n")
        if not lapped:
            with open("lap.txt", "a") as file:
                file.write(f"\n{workout_id} {user_id} {workout_name} {special_value}{special} {total_time}s")

if __name__ == "__main__":
    # This user_id is for testing
    workout(9999)
