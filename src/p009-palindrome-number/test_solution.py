import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_simple_case(self):
        integer = 123321
        expected = True
        output = Solution().isPalindrome(integer)
        self.assertEqual(output, expected)

    def test_single_digit_number(self):
        integer = 1
        expected = True
        output = Solution().isPalindrome(integer)
        self.assertEqual(output, expected)

    def test_two_digit_palindrome_number(self):
        integer = 55
        expected = True
        output = Solution().isPalindrome(integer)
        self.assertEqual(output, expected)

    def test_two_digit_non_palindrome_number(self):
        integer = 25
        expected = False
        output = Solution().isPalindrome(integer)
        self.assertEqual(output, expected)

    def test_long_even_digit_palindrome_number(self):
        integer = 96534722743569
        expected = True
        output = Solution().isPalindrome(integer)
        self.assertEqual(output, expected)

    def test_long_odd_digit_palindrome_number(self):
        integer = 9653472743569
        expected = True
        output = Solution().isPalindrome(integer)
        self.assertEqual(output, expected)

    def test_long_non_palindrome_number(self):
        integer = 92834982359359
        expected = False
        output = Solution().isPalindrome(integer)
        self.assertEqual(output, expected)

    def test_palindrome_with_same_number(self):
        integer = 33333333333
        expected = True
        output = Solution().isPalindrome(integer)
        self.assertEqual(output, expected)

    def test_zero(self):
        integer = 0
        expected = True
        output = Solution().isPalindrome(integer)
        self.assertEqual(output, expected)

    def test_negative_palindrome_number(self):
        integer = -14641
        expected = False
        output = Solution().isPalindrome(integer)
        self.assertEqual(output, expected)

    def test_negative_non_palindrome_number(self):
        integer = -1151
        expected = False
        output = Solution().isPalindrome(integer)
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
