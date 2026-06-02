"""
This Section shows Previous Workouts in the format of Date | Workout | Time
"""

import WHConfig1 as cf

def previous_workouts(user_id):
    # Find the longest workout option name
    max_length = len(max(cf.workout_menu, key=len))
    # Underline the Headings
    print(f"\033[4m {'No.':^3} | {'Date':^10} | {'Workout':^{max_length}} | {'Time':^4} | {'m/kj':^4} \033[0m")
    with open("workout_history.txt", "r") as file:
        for workout in file:
            workouts = workout.split()
            # Check if the workout belongs to the user
            if workout.startswith(str(user_id)):
                # Print the workouts that belong to the user
                print(f" {workouts[1]:^3} | {workouts[4]} | {workouts[2]:^{max_length}} | {workouts[5]:^6} | {workouts[3]:^4}")
    select = input("Select a workout to view the lap times: ")
    with open("lap.txt", "r") as file:
        for lap in file:
            if lap.startswith(select):
                lap_data = lap.split()[2:]
                lap_it = iter(lap_data)
                lap_pairs = list(zip(lap_it, lap_it))
                print(f"\033[4m {"distance"} | {"time"} \033[0m")
                for pair in lap_pairs:
                    print(f" {pair[0]:^8} | {pair[1]}")
            elif select not in lap[0]:
                print("Workout does not have further laps.")
                return
if __name__ == "__main__":
    previous_workouts(6)