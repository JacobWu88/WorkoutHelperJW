import time
import WHConfig1 as cf

"""
This section is for the workout.
"""

def workout(user_id):
    workout_name = input("What workout do you want to do? ").upper()
    if workout_name in cf.workout_menu:
        if workout_name in cf.kilometres:
         special = "Distance"
        elif workout_name in ("high jump", "gym"):
         special = "Kilojoule"
        # Give each workout a unique ID
        try:
            with open("workout_history.txt", "r") as file:
                workout_id = sum(1 for _ in file) + 1
        except FileNotFoundError:
            # If the file doesn't exist or empty, start at ID 1
            workout_id = 1
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
        while choice != "stop":
            choice = input("Enter 'L' to lap or Press Enter to stop the workout. ").lower()
            if choice == "l":
                lap_time = round(time.time() - start_time, 2)
                print(f"Lap time: {lap_time} seconds")
                if special == "Distance":
                    special_value = round(lap_time * cf.kilometres[workout_name], 2)
                elif special == "Kilojoule":
                    special_value = lap_time * 1.37
                with open("lap.txt", "a") as f:
                    f.write(f"\n{workout_id} {workout_name} {special_value} {lap_time}")
                    while choice != "stop":
                        choice = input("Enter 'L' to lap or Press Enter to stop the workout. ").lower()
                        if choice == "l":
                            lap_time = round(time.time() - start_time, 2)
                            print(f"Lap time: {lap_time} seconds")
                            f.write(f" {lap_time}")
                        elif choice == "":
                            print("Stopping Workout.")
                            choice = "stop"
            elif choice == "":
                print("Stopping Workout.")
                choice = "stop"
            else:
                print("Invalid")
        else:
            print("Invalid")
        #  End time is the time the user stopped the workout
        end_time = time.time()
        # Calculate the total time
        total_time = round(end_time - start_time, 2)
        print(f"Your workout took {total_time} seconds")
        # Write the workout to a file
        with open("workout_history.txt", "a") as file:
            file.write(f"{user_id} {workout_id} {workout_name} {special_value}km {time.strftime("%d/%m/%Y")} {total_time}\n")


if __name__ == "__main__":
    # This user_id is for testing
    workout(9999)
