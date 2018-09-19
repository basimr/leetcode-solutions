import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_no_common_prefix(self):
        strs = ['dog', 'racecar', 'car']
        expected = ''
        output = Solution.longestCommonPrefix(strs)
        self.assertEqual(expected, output, msg='Longest common prefix for "{}"'
                                               'should have been "{}"'.format(strs, expected))

    def test_simple_case(self):
        strs = ['flower', 'flow', 'flight']
        expected = 'fl'
        output = Solution.longestCommonPrefix(strs)
        self.assertEqual(expected, output, msg='Longest common prefix for "{}"'
                                               'should have been "{}"'.format(strs, expected))

    def test_one_string(self):
        strs = ['flower']
        expected = 'flower'
        output = Solution.longestCommonPrefix(strs)
        self.assertEqual(expected, output, msg='Longest common prefix for "{}"'
                                               'should have been "{}"'.format(strs, expected))

    def test_one_empty_string(self):
        strs = ['']
        expected = ''
        output = Solution.longestCommonPrefix(strs)
        self.assertEqual(expected, output, msg='Longest common prefix for "{}"'
                                               'should have been "{}"'.format(strs, expected))

    def test_all_strings_same(self):
        strs = ['flow', 'flow', 'flow']
        expected = 'flow'
        output = Solution.longestCommonPrefix(strs)
        self.assertEqual(expected, output, msg='Longest common prefix for "{}"'
                                               'should have been "{}"'.format(strs, expected))

    def test_empty_list(self):
        strs = []
        expected = ''
        output = Solution.longestCommonPrefix(strs)
        self.assertEqual(expected, output, msg='Longest common prefix for "{}"'
                                               'should have been "{}"'.format(strs, expected))


if __name__ == '__main__':
    unittest.main()
