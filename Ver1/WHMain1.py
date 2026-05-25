import WHConfig1 as cf
import WHLogReg1 as lg
import WHLockHomeScreen1 as lhs
import WHWorkout1 as wk
import WHPreviousWorkouts1 as pw

"""
This is the main script where the central logic happens.
"""

while True:
    # Lock Screen
    lhs.lock_screen()
    # Check whether if the user is logged in, define user_id. Log in or Register
    logged, user_id = lg.login_or_register()
    # Home Screen
    lhs.home_screen()

    while True:
        # Print the main menu
        cf.print_menu(cf.menu)
        menu_option = input("what do you want to do? ").lower()
        if menu_option == "workout":
            # Print the workout menu
            cf.print_menu(cf.workout_menu)
            # Bring the user_id in so it can record the workout
            wk.workout(user_id)
        elif menu_option == "previous workouts":
            pw.previous_workouts(user_id)
        # Contact Us
        elif menu_option == "contact Us":
            pass
        elif menu_option == "logout" or menu_option == "log out":
            print("Logging out...")
            exit()
        else:
            print("Invalid Input!")



