from datetime import datetime


class Habit:
    """
    A class to represent a habit.

    :param name: The name of the habit.
    :param specification: A description of the habit.
    :param periodicity: How often the habit is performed (in days).
    """

    def __init__(self, name: str, specification: str, periodicity: int):
        self.name = name
        self.specification = specification
        self.periodicity = periodicity
        self.creation_date = datetime.now()
        self.history = []

    @property
    def streak(self) -> int:
        """The streak of the habit."""
        if len(self.history) == 0:
            return 0
        else:
            # Count the number of days in a row that the habit has been done.
            streak = 1
            for i in range(len(self.history) - 1, 0, -1):
                if (self.history[i] - self.history[i - 1]).days <= self.periodicity:
                    streak += 1
                else:
                    break
            return streak

    @property
    def longest_streak(self):
        """The longest streak of the habit."""
        longest_streak = 0
        streak = 1
        for i in range(len(self.history) - 1, 0, -1):
            if (self.history[i] - self.history[i - 1]).days <= self.periodicity:
                streak += 1
                if streak > longest_streak:
                    longest_streak = streak
            else:
                streak = 1
        return longest_streak

    @classmethod
    def from_sql(cls, habit) -> "Habit":
        """
        Creates a Habit object from a tuple returned by the database.
        :param habit:
        :return:
        """
        habit_obj = cls(habit[0], habit[1], habit[2])
        if habit[3] != "":
            habit_obj.history = [datetime.strptime(h, "%Y-%m-%d %H:%M:%S") for h in habit[3].split(",")]
        else:
            habit_obj.creation_date = datetime.strptime(habit[4], "%Y-%m-%d %H:%M:%S")
        return habit_obj

    def __str__(self) -> str:
        """
        Returns a string representation of the habit.
        """
        return f"{self.name} ({self.periodicity}): {self.specification}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the habit.
        """
        return f"Habit({self.name}, {self.specification}, {self.periodicity})"

    def check_off(self) -> None:
        """Checks off the habit."""
        self.history.append(datetime.now())

    def reset(self) -> None:
        """Resets the habit."""
        self.history = []

    def check_missed(self) -> bool:
        """Checks if the habit has been missed."""
        if len(self.history) == 0:
            return False
        else:
            return (datetime.now() - self.history[-1]).days > self.periodicity

    def to_sql(self) -> tuple:
        """
        Returns a tuple representation of the habit for the database.
        """
        return self.name, self.specification, self.periodicity, ",".join(
            [h.strftime("%Y-%m-%d %H:%M:%S") for h in self.history]), self.creation_date.strftime("%Y-%m-%d %H:%M:%S")
