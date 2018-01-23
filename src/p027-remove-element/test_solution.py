import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_simple_case(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected = 2
        output = Solution().removeElement(nums, val)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
