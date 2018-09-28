import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_sanity(self):
        jewels = 'aA'
        stones = 'aAAbbbb'
        expected = 3
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_no_jewels_in_stones(self):
        jewels = 'z'
        stones = 'ZZ'
        expected = 0
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
