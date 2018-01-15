import unittest

from .solution_3 import Solution


class SolutionTestCase(unittest.TestCase):
    def test_simple_case(self):
        nums = [10, 20, 30, 70, 100, 150]
        target = 220
        expected = [3, 5]
        output = Solution().twoSum(nums, target)
        self.assertEqual(output, expected)

    def test_duplicate_elements_in_solution_separated(self):
        nums = [2, 150, 2]
        target = 4
        expected = [0, 2]
        output = Solution().twoSum(nums, target)
        self.assertEqual(output, expected)

    def test_duplicate_elements_in_solution_together(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        output = Solution().twoSum(nums, target)
        self.assertEqual(output, expected)

    def test_duplicate_zeroes_in_solution(self):
        nums = [0, 4, 3, 0]
        target = 0
        expected = [0, 3]
        output = Solution().twoSum(nums, target)
        self.assertEqual(output, expected)

    def test_negative_target(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected = [2, 4]
        output = Solution().twoSum(nums, target)
        self.assertEqual(output, expected)

    def test_two_zeroes_only(self):
        nums = [0, 0]
        target = 0
        expected = [0, 1]
        output = Solution().twoSum(nums, target)
        self.assertEqual(output, expected)

    def test_mix_of_positive_and_negative_numbers(self):
        nums = [-1, -20, 2, 4, 4, -3, 60, 1, -9]
        target = 40
        expected = [1, 6]
        output = Solution().twoSum(nums, target)
        self.assertEqual(output, expected)

    def test_positive_and_negative_sum_to_zero(self):
        nums = [-10, 10]
        target = 0
        expected = [0, 1]
        output = Solution().twoSum(nums, target)
        self.assertEqual(output, expected)

    def test_positive_and_negative_sum_to_zero_among_other_numbers(self):
        nums = [-20, -10, -19, 5, 10, 21, 50, -7]
        target = 0
        expected = [1, 4]
        output = Solution().twoSum(nums, target)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
