import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_sanity(self):
        n = 15
        expected = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ]
        output = Solution().fizzBuzz(n)
        self.assertListEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
