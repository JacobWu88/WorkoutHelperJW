"""
This Section shows Previous Workouts in the format of Date | Workout | Time
"""

import WHConfig1 as cf

def previous_workouts(user_id):
    # Find the longest workout option name
    max_length = len(max(cf.workout_menu, key=len))
    # Underline the Headings
    print(f"\033[4m{'Date':^10} | {'Workout':^{max_length}} | {'Time'} \033[0m")
    with open("workout_history.txt", "r") as file:
        for workout in file:
            workouts = workout.split()
            # Check if the workout belongs to the user
            if workout.startswith(str(user_id)):
                # Print the workouts that belong to the user
                print(f"{workouts[4]} | {workouts[2]:^{max_length}} | {workouts[5]}")

if __name__ == "__main__":
    previous_workouts(9999)