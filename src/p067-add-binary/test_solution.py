import unittest

from solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_example_1(self):
        num1 = "11"
        num2 = "1"
        expected = "100"
        output = Solution().addBinary(num1, num2)
        self.assertEqual(expected, output)

    def test_example_2(self):
        num1 = "1010"
        num2 = "1011"
        expected = "10101"
        output = Solution().addBinary(num1, num2)
        self.assertEqual(expected, output)

    def test_case_1(self):
        num1 = "0"
        num2 = "0"
        expected = "0"
        output = Solution().addBinary(num1, num2)
        self.assertEqual(expected, output)

    def test_case_2(self):
        num1 = "0"
        num2 = "1"
        expected = "1"
        output = Solution().addBinary(num1, num2)
        self.assertEqual(expected, output)

    def test_case_3(self):
        num1 = "1"
        num2 = "1"
        expected = "10"
        output = Solution().addBinary(num1, num2)
        self.assertEqual(expected, output)

    def test_case_4(self):
        num1 = "1111"
        num2 = "0"
        expected = "1111"
        output = Solution().addBinary(num1, num2)
        self.assertEqual(expected, output)

    def test_case_5(self):
        num1 = "1111"
        num2 = "1"
        expected = "10000"
        output = Solution().addBinary(num1, num2)
        self.assertEqual(expected, output)

    def test_case_6(self):
        num1 = "1110"
        num2 = "1"
        expected = "1111"
        output = Solution().addBinary(num1, num2)
        self.assertEqual(expected, output)

    def test_case_7(self):
        num1 = "11011"
        num2 = "1"
        expected = "11100"
        output = Solution().addBinary(num1, num2)
        self.assertEqual(expected, output)

    def test_case_8(self):
        num1 = "10101010"
        num2 = "11001100"
        expected = "101110110"
        output = Solution().addBinary(num1, num2)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
