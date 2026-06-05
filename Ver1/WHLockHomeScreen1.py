import time

def lock_screen():
    print("Welcome!")
    print("This is the Workout Helper, for all your workout needs!")
    return

def home_screen():
    # Display the current date and time
    current_Date = time.strftime("%d/%m/%Y")
    current_Time = time.strftime("%H:%M:%S")
    print(f"Date: {current_Date}")
    print(f"Time: {current_Time}")
    print("Note: you can choose 'back' to go back to the main menu.")
    return





