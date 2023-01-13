import unittest
from habit import Habit
from datetime import datetime, timedelta

class TestHabit(unittest.TestCase):
    def test_streak(self):
        habit = Habit("test", "test", 1)
        habit.history = [datetime(2022, 1, 1), datetime(2022, 1, 2), datetime(2022, 1, 3)]
        self.assertEqual(3, habit.streak)

    def test_longest_streak(self):
        habit = Habit("test", "test", 1)
        habit.history = [datetime(2022, 1, 1), datetime(2022, 1, 2), datetime(2022, 1, 3), datetime(2022, 1, 5),
                         datetime(2022, 1, 6)]
        self.assertEqual(3, habit.longest_streak)

    def test_longest_streak_2(self):
        habit = Habit("test", "test", 1)
        habit.history = [datetime(2022, 1, 1), datetime(2022, 1, 2), datetime(2022, 1, 3), datetime(2022, 1, 4),
                         datetime(2022, 1, 6), datetime(2022, 1, 7)]
        self.assertEqual(4, habit.longest_streak)

    def test_check_missed(self):
        habit = Habit("test", "test", 1)
        habit.history = [datetime.now()-timedelta(days=1)]
        self.assertFalse(habit.check_missed())

    def test_reset(self):
        habit = Habit("test", "test", 1)
        habit.history = [datetime.now()]
        habit.reset()
        self.assertEqual([], habit.history)

    def test_check_off(self):
        habit = Habit("test", "test", 1)
        habit.check_off()
        self.assertEqual(1, len(habit.history))


if __name__ == '__main__':
    unittest.main()
