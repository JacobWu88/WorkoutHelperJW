"""
This Section shows Previous Workouts in the format of Date | Workout | Time
"""

import WHConfig1 as cf

def previous_workouts(user_id):
    # Find the longest workout option name
    max_length = len(max(cf.workout_menu, key=len))
    max_time = len(max(cf.workout_menu, key=len))
    # Underline the Headings
    print(f"\033[4m {'No.':^3} | {'Date':^10} | {'Workout':^{max_length}} | {'Time':^6} | {'m/kj':^4} \033[0m")
    with open("workout_history.txt", "r") as file:
        for workout in file:
            workouts = workout.split()
            # Check if the workout belongs to the user
            if workout.startswith(str(user_id)):
                # Print the workouts that belong to the user
                print(f" {workouts[1]:^3} | {workouts[4]} | {workouts[2]:^{max_length}} | {workouts[5]:^6} | {workouts[3]:^4}")
    while True:
        select = input("Select a workout to view the lap times: ")
        if select.lower() == "back":
            break

        found_workout = False
        with open("lap.txt", "r") as file:
            for lap in file:
                # If workout selected is in the lap file and matches
                if lap.startswith(select):
                    found_workout = True
                    if select == "":
                        print("Invalid Input!")
                    elif str(user_id) == lap.split()[1]:
                        # Skip the first 2 parts
                        lap_data = lap.split()[3:]
                        lap_it = iter(lap_data)
                        lap_pairs = list(zip(lap_it, lap_it))
                        print(f"\033[4m {'distance'} | {'time'} \033[0m")
                        for pair in lap_pairs:
                            print(f" {pair[0]:^8} | {pair[1]}")
                    else:
                        print("You don't have permission to view this workout.")
                    break

        if not found_workout:
            print("Invalid Input!")




if __name__ == "__main__":
    previous_workouts(9999)