from distanceBetweenDays.distance_between_days import DistanceBetweenDays
import unittest


class Testtest_DistanceBetweenDays(unittest.TestCase):
    def test_DistanceBetweenDays(self):
        self.assertEqual(DistanceBetweenDays("2/6/1983", "22/6/1983").get_difference(), 19, "Should be 19")
        self.assertEqual(DistanceBetweenDays("4/7/1984", "25/12/1984").get_difference(), 173, "Should be 173")
        self.assertEqual(DistanceBetweenDays("3/1/1989", "3/8/1983").get_difference(), 2036, "Should be 19")


if __name__ == "__main__":
    unittest.main()