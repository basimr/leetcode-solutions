import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_simple_case(self):
        nums = [1, 1, 2]
        expected = 2
        output = Solution.removeDuplicates(nums)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
