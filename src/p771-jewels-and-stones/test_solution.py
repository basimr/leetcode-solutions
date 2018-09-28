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

    def test_no_jewels_no_stones(self):
        jewels = ''
        stones = ''
        expected = 0
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_no_jewels_one_stone(self):
        jewels = ''
        stones = 'g'
        expected = 0
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_no_jewels_many_stones(self):
        jewels = ''
        stones = 'asdkowidlk'
        expected = 0
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_one_jewel_no_stones(self):
        jewels = 'a'
        stones = ''
        expected = 0
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_one_jewel_one_stone_match(self):
        jewels = 'a'
        stones = 'a'
        expected = 1
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_one_jewel_one_stone_no_match(self):
        jewels = 'a'
        stones = 'b'
        expected = 0
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_one_jewel_many_stones_match(self):
        jewels = 'a'
        stones = 'jksaea'
        expected = 2
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_many_jewels_no_stones(self):
        jewels = 'abc'
        stones = ''
        expected = 0
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_many_jewels_one_stone_match(self):
        jewels = 'abc'
        stones = 'b'
        expected = 1
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_many_jewels_one_stone_no_match(self):
        jewels = 'abc'
        stones = 'k'
        expected = 0
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_many_jewels_many_stones_match(self):
        jewels = 'abcde'
        stones = 'bcd'
        expected = 3
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_many_jewels_many_stones_no_match(self):
        jewels = 'abcdefg'
        stones = 'hijklmnop'
        expected = 0
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_all_jewels_match_once(self):
        jewels = 'abcdefg'
        stones = 'abcdefg'
        expected = 7
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_all_jewels_match_once_shuffled_order(self):
        jewels = 'abcdefg'
        stones = 'egabcfd'
        expected = 7
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_mixed_case_no_matches(self):
        jewels = 'aBcDeFg'
        stones = 'AbCdEfG'
        expected = 0
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_mixed_case_with_matches(self):
        jewels = 'aBcDeFg'
        stones = 'zyDaFwx'
        expected = 3
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_match_at_beginning(self):
        jewels = 'a'
        stones = 'azyDFwx'
        expected = 1
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_match_at_middle(self):
        jewels = 'a'
        stones = 'zyDaFwx'
        expected = 1
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)

    def test_match_at_end(self):
        jewels = 'a'
        stones = 'zyDFwxa'
        expected = 1
        output = Solution().numJewelsInStones(jewels, stones)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
