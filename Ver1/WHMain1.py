import WHConfig1
import WHLogReg1
import WHLockHomeScreen1


while True:
    # Lock Screen
    WHLockHomeScreen1.lock_screen()
    # Log in or Register
    WHLogReg1.login_or_register()
    # Home Screen
    WHLockHomeScreen1.home_screen()
    # Print the main menu
    WHConfig1.print_menu()

    while True:
        menu_option = input("what do you want to do?").lower()

        if menu_option == "workout":
            pass
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



