"""
This section is for the workout.
"""

import time
import WHConfig as cf

def workout(user_id):
    # Convert the time to the correct unit
    def convert(timing):
        converted = timing * multiplier
        return converted
    while True:
        workout_name = input("What workout do you want to do? (or go 'back') ").upper()
        if workout_name == "BACK":
            break
        if workout_name in cf.number_to_workout.keys():
            workout_name = cf.number_to_workout.get(workout_name)
        if workout_name in cf.workout_menu:
            # Define the unit of the workout
            if workout_name in cf.kilometres:
             special = "m"
            elif workout_name in cf.kilojoules:
             special = "Kj"
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

            # Lap data is a list of lap times
            lap_data = []
            while True:
                # Lap
                choice = input("Enter 'L' to lap or Press Enter to stop the workout. ").lower()
                if choice == "l":
                    # Calculate the lap time
                    lap_time = round(time.time() - start_time, 2)
                    special_value = round(convert(lap_time), 2)
                    print(f"Lap time: {lap_time} seconds")
                    # Add the lap time to the lap_data list
                    lap_data.append(f"{special_value}{special} {lap_time}s")
                # End workout
                elif choice == "":
                    print("Stopping Workout.")
                    break
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
                # Write the workout to the workout file
                file.write(f"{user_id} {workout_id} {workout_name} {special_value}{special} {time.strftime('%d/%m/%Y')} {total_time}    \n")

                with open("lap.txt", "a") as f:
                    # If there are laps, write them to the lap file
                    if lap_data:
                        f.write(f"\n{workout_id} {user_id} {workout_name} {' '.join(lap_data)}")
                    # If there are no laps, write the total time to the lap file
                    else:
                        f.write(f"\n{workout_id} {user_id} {workout_name} {special_value}{special} {total_time}s")
        else:
            print("Invalid Workout")
if __name__ == "__main__":
    # This user_id is for testing
    workout(9999)
