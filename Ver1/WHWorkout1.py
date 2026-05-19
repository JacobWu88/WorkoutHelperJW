import time

def workout(user_id):
    workout_name = input("What workout do you want to do? ").lower()
    if workout_name in ("walk", "run", "bike", "basketball", "skating", "badminton"):
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("GO!")
        # Start time is the current time
        start_time = time.time()
        input("Press Enter to stop the workout")
        #  End time is the time the user stopped the workout
        end_time = time.time()
        # Calculate the total time
        total_time = end_time - start_time
        print(f"Your workout took {round(total_time, 2)} seconds")
        # Write the workout to a file
        with open("workout_history.txt", "a") as file:
            file.write(f"{user_id} {workout_name} {round(total_time, 2)}\n")


if __name__ == "__main__":
    # This user_id is for testing
    workout(9999)
