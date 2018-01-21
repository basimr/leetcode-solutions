import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_empty_string(self):
        s = ''
        expected = True
        output = Solution.isValid(s)
        self.assertEqual(expected, output, msg='String "{}" should be considered valid'.format(s))

    def test_trivial_cases(self):
        cases = ['()', '{}', '[]']
        expected = True
        for s in cases:
            output = Solution.isValid(s)
            self.assertEqual(expected, output, msg='String "{}" should be considered valid'.format(s))

    def test_invalid_cases(self):
        cases = [
            '(('
            '(((((',
            '}',
            '({)[][][}',
            '[[({())[]([)]}]]',
        ]
        expected = False
        for s in cases:
            output = Solution.isValid(s)
            self.assertEqual(expected, output, msg='String "{}" should not be considered valid'.format(s))

    def test_valid_shallowly_nested_parentheses(self):
        s = '[][][][][][]'
        expected = True
        output = Solution.isValid(s)
        self.assertEqual(expected, output, msg='String "{}" should be considered valid'.format(s))

    def test_valid_deeply_nested_parentheses(self):
        cases = [
            '[[[[[[[[[[]]]]]]]]]]',
            '({[({[({[]})]})]})',
        ]
        expected = True
        for s in cases:
            output = Solution.isValid(s)
            self.assertEqual(expected, output, msg='String "{}" should be considered valid'.format(s))


if __name__ == '__main__':
    unittest.main()
