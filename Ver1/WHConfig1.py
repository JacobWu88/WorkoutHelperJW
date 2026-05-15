menu = ["Workout", "Summary", "Previous Workouts", "Milestones", "Profile", "Contact Us", "Log Out"]
def print_menu():
    line = "-" * len("|".join(menu))
    print(line)
    print("|".join(menu))
    print(line)

if __name__ == "__main__":
    print_menu()