workouts = []


def main():
    print("This is a fitness tracker app(in development)")
    print("1. Add workout")
    print("2. View workout history")
    print("3. Exit")


def add_workout():
    workout = input("Enter your workout: ")
    workouts.append(workout)
    print("Workout added!")


def view_workout_history():
    for i, workout in enumerate(workouts, start=1):
        print(f"{i}. {workout}. ")


main()
choice = input("Choose option: ")
if choice == "1":
    add_workout()
elif choice == "2":
    view_workout_history()
elif choice == "3":
    print("Exiting the app. ")
