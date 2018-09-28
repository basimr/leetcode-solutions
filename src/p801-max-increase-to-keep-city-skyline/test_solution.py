import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_sanity(self):
        grid = [
            [3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0],
        ]
        expected = 5 + 4 + 0 + 3 \
                   + 5 + 0 + 2 + 0 \
                   + 0 + 2 + 2 + 4 \
                   + 3 + 0 + 2 + 3
        output = Solution().maxIncreaseKeepingSkyline(grid)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
