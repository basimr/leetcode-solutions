import unittest

from solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_example_1(self):
        string = "Hello World"
        expected = 5
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_example_2(self):
        string = "    fly  me  to the    moon     "
        expected = 4
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_example_3(self):
        string = "luffy is still joyboy"
        expected = 6
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_case_1(self):
        string = "a"
        expected = 1
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_case_2(self):
        string = "   a    "
        expected = 1
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_case_3(self):
        string = " a a a a a a "
        expected = 1
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_case_4(self):
        string = "aaaaaaaa"
        expected = 8
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_case_5(self):
        string = "aa"
        expected = 2
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_case_6(self):
        string = "aaa"
        expected = 3
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_case_7(self):
        string = " a"
        expected = 1
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_case_8(self):
        string = "a "
        expected = 1
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_case_9(self):
        string = "aa "
        expected = 2
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)

    def test_case_10(self):
        string = " aa"
        expected = 2
        output = Solution().lengthOfLastWord(string)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
