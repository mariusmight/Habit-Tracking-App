# Habit-Tracking-App

In order to creat the habit tracking app I needed to store the name, periodicity and the history of each habit
where the history would be a list of the dates when the habit was checked off and would be used to calculate the
streaks.

In order to store the data I decided to use a sqlite3 database which would be created and managed using the db.py file.
the usage of sqlite3 was chosen because it is a lightweight database that is easy to use and does not require a server
to run.

In order to develop the application I used a while loop that would ask the user for input and then execute the
corresponding function.
The functions that were used are:
add_habit() - adds a habit to the database
view_habits() - prints all the habits in the database
check_habit() - checks off a habit for the current day
reset_habit() - resets the history of a habit
display_statistics() - displays the statistics of a habit
init_habits() - initialize 5 predefined habits
quit() - quits the application

The Habit class represents a habit that a person may have. It has the following attributes:

- `name`: a string representing the name of the habit.
- `specification`: a string describing the habit.
- `periodicity`: an integer representing how often the habit is performed, in days.
- `creation_date`: a datetime object representing the date and time that the habit was created.
- `history`: a list of datetime objects representing the dates and times that the habit was completed.

The Habit class has the following methods:

- `__init__`: a constructor method that initializes the name, specification, and periodicity attributes, and sets the creation_date attribute to the current date and time, and the history attribute to an empty list.
- `streak`: a `@property` decorator that returns an integer representing the number of consecutive days that the habit has been completed.
- `longest_streak`: a `@property` decorator that returns an integer representing the longest streak of consecutive days that the habit has been completed.
- `from_sql`: a class method that creates a Habit object from a tuple returned by a database.
- `__str__`: a method that returns a string representation of the habit.
- `__repr__`: a method that returns a string representation of the habit.
- `check_off`: a method that adds the current date and time to the history attribute.
- `reset`: a method that sets the history attribute to an empty list.
- `check_missed`: a method that returns a boolean indicating whether the habit has been missed (i.e., it has not been completed within the required periodicity).
- `to_sql`: a method that returns a tuple representation of the habit that can be stored in a database.

## Requirements

- python 3.6 or higher
- tabulate
  you can install tabulate with `pip install tabulate`

## Usage

- `python3 main.py` to run the program
