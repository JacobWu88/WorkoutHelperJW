import WHConfig1 as cf
import WHLogReg1 as lg
import WHLockHomeScreen1 as lhs
import WHWorkout1 as wk


while True:
    # Lock Screen
    lhs.lock_screen()
    # Log in or Register
    lg.login_or_register()
    # Home Screen
    lhs.home_screen()
    # Print the main menu
    cf.print_menu(cf.menu)

    while True:
        menu_option = input("what do you want to do? ").lower()
        if menu_option == "workout":
            cf.print_menu(cf.workout_menu)
            wk.workout()
        elif menu_option == "summary":
            pass
        elif menu_option == "milestones":
            pass
        elif menu_option == "profile":
            pass
        elif menu_option == "contact Us":
            pass
        elif menu_option == "logout" or menu_option == "log out":
            print("Logging out...")
            break
        else:
            print("Invalid Input!")



