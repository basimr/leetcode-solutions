import unittest

from .solution import Solution, MAX_32_BIT_SIGNED_INTEGER, MIN_32_BIT_SIGNED_INTEGER


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

    def test_min_32_bit_signed_integer_overflow(self):
        integer = MIN_32_BIT_SIGNED_INTEGER
        expected = 0
        output = Solution().reverse(integer)
        self.assertEqual(output, expected)


class UtilityTestCase(unittest.TestCase):
    def test_compute_num_digits(self):
        number = 123
        expected = 3
        output = Solution().compute_num_digits(number)
        self.assertEqual(output, expected)

    def test_compute_num_digits_trailing_zeros(self):
        for number, num_digits in [(10**x, x+1) for x in range(1, 10)]:
            output = Solution().compute_num_digits(number)
            self.assertEqual(output, num_digits)

    def test_compute_num_digits_zero(self):
        number = 0
        expected = 1
        output = Solution().compute_num_digits(number)
        self.assertEqual(output, expected)

    def test_compute_num_digits_square_numbers(self):
        self.assertEqual(Solution().compute_num_digits(1), 1)
        self.assertEqual(Solution().compute_num_digits(4), 1)
        self.assertEqual(Solution().compute_num_digits(9), 1)
        self.assertEqual(Solution().compute_num_digits(16), 2)
        self.assertEqual(Solution().compute_num_digits(25), 2)
        self.assertEqual(Solution().compute_num_digits(36), 2)
        self.assertEqual(Solution().compute_num_digits(100), 3)


if __name__ == '__main__':
    unittest.main()
