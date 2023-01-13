from db import *
from habit import Habit
import tabulate as tabulate

habits_list = []


def check_missed():
    """Checks if any habits have been missed."""
    global habits_list
    for habit in habits_list:
        if habit.check_missed():
            print(f"You missed a habit: {habit.name} ({habit.periodicity})")
            print(f"Last time you did it was {habit.history[-1]}")
            print("resetting...")
            print("====================================")
            habit.reset()


def add_habit():
    """Asks for habit details and adds it to the database."""
    global habits_list
    name = input("Enter the name of the habit: ")
    specification = input("Enter a description of the habit: ")
    try:
        while True:
            periodicity = input("Enter the periodicity of the habit (in days): ")
            periodicity = int(periodicity)
            if periodicity > 0:
                break
            print("Invalid periodicity. Try again.")
        habit = Habit(name, specification, periodicity)
        habits_list.append(habit)
        save_habit(habit)
        print(f"Added {habit.name} to the database.")
        print("====================================")
    except: 
        Exception 
        print ("Invalid periodicity. Try again.")


def view_habits():
    """Displays all habits."""
    global habits_list
    if len(habits_list) == 0:
        print("No habits found.")
        print("====================================")
        return
    print("Habits Table:")
    headers = ["Name", "Specification", "Periodicity", "Streak", "History"]
    table = [(habit.name, habit.specification, habit.periodicity, habit.streak, ",".join(
        [h.strftime("%Y-%m-%d %H:%M:%S") for h in habit.history])) for habit in habits_list]
    print(tabulate.tabulate(table, headers=headers, tablefmt="grid"))
    print("====================================")


def check_habit():
    """Checks off a habit."""
    global habits_list
    name = input("Enter the name of the habit: ")
    for habit in habits_list:
        if habit.name == name:
            habit.check_off()
            update_habit(habit)
            print(f"Checked off {habit.name}.")
            print("====================================")
            return
    print("Habit not found.")
    print("====================================")


def reset_habit():
    """Resets a habit."""
    global habits_list
    name = input("Enter the name of the habit: ")
    for habit in habits_list:
        if habit.name == name:
            habit.reset()
            update_habit(habit)
            print(f"Reset {habit.name}.")
            print("====================================")
            return
    print("Habit not found.")
    print("====================================")


def get_longest_streak():
    """Returns the longest streak of all habits."""
    global habits_list
    longest_streak = 0
    for habit in habits_list:
        if habit.streak > longest_streak:
            longest_streak = habit.streak
    return longest_streak


def display_statistics():
    """Displays statistics about the habits."""
    global habits_list
    print("Statistics:")
    print("====================================")
    print(f"Longest streak: {get_longest_streak()}")
    print("====================================")
    headers = ["Name", "Specification", "Periodicity", "Streak", "History"]
    table = [(habit.name, habit.specification, habit.periodicity, habit.streak, ",".join(
        [h.strftime("%Y-%m-%d %H:%M:%S") for h in habit.history])) for habit in habits_list if habit.periodicity == 1]
    if len(table) > 0:
        print("Daily Habits:")
        print(tabulate.tabulate(table, headers=headers, tablefmt="grid"))
    else:
        print("No daily habits found.")
    print("====================================")
    headers = ["Name", "Specification", "Periodicity", "Streak", "History"]
    table = [(habit.name, habit.specification, habit.periodicity, habit.streak, ",".join(
        [h.strftime("%Y-%m-%d %H:%M:%S") for h in habit.history])) for habit in habits_list if habit.check_missed()]
    if len(table) > 0:
        print(f'Habits I struggled with last month:')
        print(tabulate.tabulate(table, headers=headers, tablefmt="grid"))
    else:
        print("No habits I struggled with last month.")
    print("====================================")


def init_habits():
    global habits_list
    habits = get_habits()
    habits_list = [Habit.from_sql(habit) for habit in habits]
    if len(habits_list) == 0:
        # if there are no habits in the database, add some
        habit = Habit("Exercise", "Go for a run", 1)
        habits_list.append(habit)
        save_habit(habit)
        habit = Habit("Meditate", "Meditate for 10 minutes", 1)
        habits_list.append(habit)
        save_habit(habit)
        habit = Habit("Read", "Read for 30 minutes", 1)
        habits_list.append(habit)
        save_habit(habit)
        habit = Habit("Drink Water", "Drink 2 litres of water", 1)
        habits_list.append(habit)
        save_habit(habit)
        habit = Habit("Visit Parents", "Visit parents", 7)
        habits_list.append(habit)
        save_habit(habit)


def main():
    global habits_list
    print("Welcome to the Habit Tracker!")
    print("====================================")
    # load habits from database
    init_db()
    init_habits()
    # main loop
    while True:
        # check if any habits have been missed
        check_missed()

        print("What would you like to do?")
        print("1. Add a new habit")
        print("2. View all habits")
        print("3. Check off a habit")
        print("4. Reset a habit")
        print("5. View statistics")
        print('6. List habits with X periodicity')
        print("7. Show longest streak for specific habit")
        print("0. Exit")
        print("====================================")
        choice = input("> ")
        if choice == "1":
            add_habit()
        elif choice == "2":
            view_habits()
        elif choice == "3":
            check_habit()
        elif choice == "4":
            reset_habit()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            periodicity = input("Enter periodicity: ")
            periodicity = int(periodicity)
            headers = ["Name", "Specification", "Periodicity", "Streak", "History"]
            table = [(habit.name, habit.specification, habit.periodicity, habit.streak, ",".join(
                [h.strftime("%Y-%m-%d %H:%M:%S") for h in habit.history])) for habit in habits_list if habit.periodicity == periodicity]
            if len(table) > 0:
                print(f'Habits with periodicity {periodicity}:')
                print(tabulate.tabulate(table, headers=headers, tablefmt="grid"))
            else:
                print(f"No habits with periodicity {periodicity}.")
            print("====================================")
        elif choice == "7":
            name = input("Enter habit name: ")
            for habit in habits_list:
                if habit.name == name:
                    print(f"Longest streak for {habit.name}: {habit.longest_streak}")
                    print("====================================")
                    return
            print("Habit not found.")
            print("====================================")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()