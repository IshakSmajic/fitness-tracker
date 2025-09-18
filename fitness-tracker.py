def main():
    print("This is a fitness tracker app(in development)")
    print("1. Add workout")
    print("2. View workout history")
    print("3. Exit")


def add_workout():
    print("Placement function for adding a workout")


def view_workout_history():
    print("Placement function for viewing workout history")


main()
choice = input("Choose option: ")
if choice == "1":
    add_workout()
elif choice == "2":
    view_workout_history()
elif choice == "3":
    print("Exiting the app")
