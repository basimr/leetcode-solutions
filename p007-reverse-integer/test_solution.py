import unittest

from .solution import Solution, MAX_32_BIT_SIGNED_INTEGER


class SolutionTestCase(unittest.TestCase):
    def test_simple_case(self):
        integer = 123
        expected = 321
        output = Solution().reverse(integer)
        self.assertEqual(output, expected)

    def test_negative_integer(self):
        integer = -123
        expected = -321
        output = Solution().reverse(integer)
        self.assertEqual(output, expected)

    def test_trailing_zero(self):
        integer = 120
        expected = 21
        output = Solution().reverse(integer)
        self.assertEqual(output, expected)

    def test_multiple_trailing_zeros(self):
        integer = 12000
        expected = 21
        output = Solution().reverse(integer)
        self.assertEqual(output, expected)

    def test_negative_trailing_zero(self):
        integer = -120
        expected = -21
        output = Solution().reverse(integer)
        self.assertEqual(output, expected)

    def test_negative_multiple_trailing_zeros(self):
        integer = -12000
        expected = -21
        output = Solution().reverse(integer)
        self.assertEqual(output, expected)

    def test_zero(self):
        integer = 0
        expected = 0
        output = Solution().reverse(integer)
        self.assertEqual(output, expected)

    def test_single_digit_integer(self):
        integer = 1
        expected = 1
        output = Solution().reverse(integer)
        self.assertEqual(output, expected)

    def test_negative_single_digit_integer(self):
        integer = -1
        expected = -1
        output = Solution().reverse(integer)
        self.assertEqual(output, expected)

    def test_max_32_bit_signed_integer_overflow(self):
        integer = MAX_32_BIT_SIGNED_INTEGER
        expected = 0
        output = Solution().reverse(integer)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
