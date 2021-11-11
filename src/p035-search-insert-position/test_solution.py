import unittest

from solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 3, 5, 6]
        target = 5
        expected = 2
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)

    def test_example_2(self):
        nums = [1, 3, 5, 6]
        target = 2
        expected = 1
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)

    def test_example_3(self):
        nums = [1, 3, 5, 6]
        target = 7
        expected = 4
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)

    def test_example_4(self):
        nums = [1, 3, 5, 6]
        target = 0
        expected = 0
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)

    def test_example_5(self):
        nums = [1]
        target = 0
        expected = 0
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)

    def test_negative_retreival(self):
        nums = [-10, -5, 0, 5, 10]
        target = -10
        expected = 0
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)

    def test_negative_insertion(self):
        nums = [-10, -5, 0, 5, 10]
        target = -7
        expected = 1
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)

    def test_insert_at_end_negative_numbers(self):
        nums = [-10, -5, -4, -2]
        target = -1
        expected = 4
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)

    def test_insert_at_end_positive_numbers(self):
        nums = [100, 200, 1000, 9999]
        target = 10000
        expected = 4
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)

    def test_insert_at_start_with_one_number(self):
        nums = [1]
        target = 0
        expected = 0
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)

    def test_insert_at_end_with_one_number(self):
        nums = [1]
        target = 2
        expected = 1
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)

    def test_insert_at_start_with_same_number(self):
        nums = [1]
        target = 1
        expected = 0
        output = Solution().searchInsert(nums, target)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
