import data
import lab5
import unittest

from data import Point


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    from data import Time
    def test_time_add_1(self):
        time1 = data.Time(5,59,59)
        time2 = data.Time(2,5,5)
        expected = data.Time(8,5,4)
        actual = lab5.time_add(time1, time2)
        self.assertEqual(expected, actual)

    def test_time_add_2(self):
        time1 = data.Time(5,20,32)
        time2 = data.Time(7,48,21)
        expected = data.Time(13,8,53)
        actual = lab5.time_add(time1, time2)
        self.assertEqual(expected, actual)

    # Part 4

    def test_is_descending_1(self):
        input = [5.0,2,3.5,1]
        expected = False
        actual = lab5.is_descending(input)
        self.assertEqual(expected, actual)

    def test_is_descending_2(self):
        input = [6, 5.5, 5.1, 0, -0.1, -5]
        expected = True
        actual = lab5.is_descending(input)
        self.assertEqual(expected, actual)

    # Part 5
    def test_largest_between_1(self):
        input_nums = [4,1,5,8,13,4]
        index_1 = 2
        index_2 = 4
        expected = 4
        actual = lab5.largest_between(input_nums, index_1, index_2)
        self.assertEqual(expected,actual)

    def test_largest_between_2(self):
        input_nums = [-5, 6, 2, 5, 33, 1]
        index_1 = -5
        index_2 = 10
        expected = 4
        actual = lab5.largest_between(input_nums, index_1, index_2)
        self.assertEqual(expected, actual)

    def test_largest_between_3(self):
        input_nums = [-5, 6, 2, 5, 33, 1]
        index_1 = 5
        index_2 = 4
        expected = None
        actual = lab5.largest_between(input_nums, index_1, index_2)
        self.assertEqual(expected, actual)

    def test_largest_between_4(self):
        input_nums = []
        index_1 = 0
        index_2 = 0
        expected = None
        actual = lab5.largest_between(input_nums, index_1, index_2)
        self.assertEqual(expected, actual)

    # Part 6
    from data import Point

    def test_furthest_from_origin_1(self):
        input = [data.Point(0, 0),
                 data.Point(5, 0),
                 data.Point(5,-5)]
        expected = 2
        actual = lab5.furthest_from_origin(input)
        self.assertEqual(expected, actual)

    def test_furthest_from_origin_2(self):
        input = []
        expected = None
        actual = lab5.furthest_from_origin(input)
        self.assertEqual(expected, actual)

    def test_furthest_from_origin_3(self):
        input = [Point(3,4),
                 Point(6, 5),
                 Point(-1,-2)]
        expected = 1
        actual = lab5.furthest_from_origin(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
