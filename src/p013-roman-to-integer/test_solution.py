import unittest

from .solution import Solution, ROMAN_TO_INT


class SolutionTestCase(unittest.TestCase):
    def test_single_letter_numbers(self):
        for roman, integer in ROMAN_TO_INT.items():
            output = Solution().romanToInt(roman)
            self.assertEqual(output, integer)

    def test_roman_numbers_with_repeated_letters(self):
        cases = {
            'IIII': 4,
            'XXX': 30,
            'CC': 200,
            'MMM': 3000,
        }
        for roman, integer in cases.items():
            output = Solution().romanToInt(roman)
            self.assertEqual(output, integer)

    def test_roman_numbers_without_subtractive_notation(self):
        cases = {
            'VI': 6,
            'VIII': 8,
            'XII': 12,
            'XV': 15,
            'XVII': 17,
            'MMMDCCCCLXXXXVIIII': 3999,
        }
        for roman, integer in cases.items():
            output = Solution().romanToInt(roman)
            self.assertEqual(output, integer)

    def test_roman_numbers_with_subtractive_notation(self):
        cases = {
            'IV': 4,
            'XIV': 14,
            'XXIV': 24,
            'IM': 999,
            'XLV': 45,
            'XIX': 19,
        }
        for roman, integer in cases.items():
            output = Solution().romanToInt(roman)
            self.assertEqual(output, integer)


if __name__ == '__main__':
    unittest.main()
