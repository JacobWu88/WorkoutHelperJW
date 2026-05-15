import time
import WHConfig1 as cf

def workout():
    workout_name = input("What workout do you want to do? ")
    if workout_name == "walk":
        print("3")
        print("2")
        print("1")
        print("GO!")
    start_time = time.time()
    input("Press Enter to stop the workout")
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Your workout took {round(total_time, 2)} seconds")
    with open("workout_history.txt", "a") as file:
        file.write(f"{cf.get_user_id()} {workout_name} {round(total_time, 2)}\n")

if __name__ == "__main__":
    workout()
