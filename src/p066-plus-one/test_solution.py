import unittest

from solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_example_1(self):
        digits = [1, 2, 3]
        expected = [1, 2, 4]
        output = Solution().plusOne(digits)
        self.assertEqual(expected, output)

    def test_example_2(self):
        digits = [4, 3, 2, 1]
        expected = [4, 3, 2, 2]
        output = Solution().plusOne(digits)
        self.assertEqual(expected, output)

    def test_example_3(self):
        digits = [0]
        expected = [1]
        output = Solution().plusOne(digits)
        self.assertEqual(expected, output)

    def test_example_4(self):
        digits = [9]
        expected = [1, 0]
        output = Solution().plusOne(digits)
        self.assertEqual(expected, output)

    def test_case_2(self):
        digits = [9, 9, 9]
        expected = [1, 0, 0, 0]
        output = Solution().plusOne(digits)
        self.assertEqual(expected, output)

    def test_case_3(self):
        digits = [4, 9, 9, 9]
        expected = [5, 0, 0, 0]
        output = Solution().plusOne(digits)
        self.assertEqual(expected, output)

    def test_case_4(self):
        digits = [2, 9, 2, 9]
        expected = [2, 9, 3, 0]
        output = Solution().plusOne(digits)
        self.assertEqual(expected, output)

    def test_case_5(self):
        digits = [5, 2, 4, 7, 9, 0, 4]
        expected = [5, 2, 4, 7, 9, 0, 5]
        output = Solution().plusOne(digits)
        self.assertEqual(expected, output)

    def test_case_6(self):
        digits = [1, 9]
        expected = [2, 0]
        output = Solution().plusOne(digits)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
