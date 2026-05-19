def previous_workouts(user_id):
    with open("workout_history.txt", "r") as file:
        for workout in file:
            if workout.startswith(str(user_id)):
                workouts = workout.split()
                print("workout:|Time:")
                print(f"{workouts[1]}     | {workouts[2]}")

if __name__ == "__main__":
    previous_workouts(9999)