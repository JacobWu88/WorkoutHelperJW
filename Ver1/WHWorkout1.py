import time

def workout(user_id):
    workout_name = input("What workout do you want to do? ").lower()
    if workout_name in ("walk", "run", "bike", "basketball", "skating", "badminton"):
        # Give each workout a unique ID
        try:
            with open("workout_history.txt", "r") as file:
                workout_id = sum(1 for _ in file) + 1
        except FileNotFoundError:
            # If the file doesn't exist or empty, start at ID 1
            workout_id = 1
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("GO!")
        # Start time is the current time
        start_time = time.time()
        distance = 0
        choice = "go"
        while choice != "stop":
            choice = input("Enter 'L' to lap or Press Enter to stop the workout. ").lower()
            if choice == "l":
                lap_time = round(time.time() - start_time, 2)
                print(f"Lap time: {lap_time} seconds")
                with open("lap.txt", "a") as f:
                    print("Opened")
                    f.write(f"\n{workout_id} {workout_name} {lap_time}")
                    print("Writing")
                    while choice != "stop":
                        choice = input("Enter 'L' to lap or Press Enter to stop the workout. ").lower()
                        if choice == "l":
                            lap_time = round(time.time() - start_time, 2)
                            f.write(f" {lap_time}")
                            print("writing")
                        elif choice == "":
                            print("Stopping Workout.")
                            choice = "stop"
            else:
                print("Invalid")
        #  End time is the time the user stopped the workout
        end_time = time.time()
        # Calculate the total time
        total_time = round(end_time - start_time, 2)
        print(f"Your workout took {total_time} seconds")
        # Write the workout to a file
        with open("workout_history.txt", "a") as file:
            file.write(f"{user_id} {workout_id} {workout_name} {distance}km {time.strftime("%d/%m/%Y")} {total_time}\n")


if __name__ == "__main__":
    # This user_id is for testing
    workout(9999)
