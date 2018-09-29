import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_sanity(self):
        s = 'abcabcbb'
        expected = 3
        output = Solution().lengthOfLongestSubstring(s)
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
