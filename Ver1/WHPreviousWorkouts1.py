def previous_workouts(user_id):
    with open("workout_history.txt", "r") as file:
        for workout in file:
            workouts = workout.split()
            print(f"Date       | {' ' * len(workouts[2])} | Time")
            if workout.startswith(str(user_id)):
                print(f"{workouts[3]} | {workouts[2]} | {workouts[4]}")

if __name__ == "__main__":
    previous_workouts(9999)