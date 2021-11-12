import unittest

from solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_example_1(self):
        num = 1
        expected = 1
        output = Solution().climbStairs(num)
        self.assertEqual(expected, output)

    def test_example_2(self):
        num = 2
        expected = 2
        output = Solution().climbStairs(num)
        self.assertEqual(expected, output)

    def test_case_1(self):
        num = 3
        expected = 3
        output = Solution().climbStairs(num)
        self.assertEqual(expected, output)

    def test_case_2(self):
        num = 4
        expected = 5
        output = Solution().climbStairs(num)
        self.assertEqual(expected, output)

    def test_case_3(self):
        num = 5
        expected = 8
        output = Solution().climbStairs(num)
        self.assertEqual(expected, output)

    def test_case_4(self):
        num = 6
        expected = 13
        output = Solution().climbStairs(num)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
