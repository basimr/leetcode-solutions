import unittest

from solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_example_1(self):
        num = 4
        expected = 2
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_example_2(self):
        num = 8
        expected = 2
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_1(self):
        num = 100
        expected = 10
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_2(self):
        num = 10000
        expected = 100
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_3(self):
        num = 64
        expected = 8
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_4(self):
        num = 42384729
        expected = 6510
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_5(self):
        num = 8239058285923085
        expected = 90769258
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_6(self):
        num = 104837121
        expected = 10239
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_7(self):
        num = 15129
        expected = 123
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_8(self):
        num = 998001
        expected = 999
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_9(self):
        num = 0
        expected = 0
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_10(self):
        num = 1
        expected = 1
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_11(self):
        num = 2
        expected = 1
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_12(self):
        num = 3
        expected = 1
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_13(self):
        num = 4
        expected = 2
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_14(self):
        num = 5
        expected = 2
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_15(self):
        num = 6
        expected = 2
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_16(self):
        num = 7
        expected = 2
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_17(self):
        num = 8
        expected = 2
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_18(self):
        num = 9
        expected = 3
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_19(self):
        num = 10
        expected = 3
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_20(self):
        num = 16
        expected = 4
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_21(self):
        num = 208027
        expected = 456
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_22(self):
        num = 208757
        expected = 456
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_22(self):
        num = 2147483648
        expected = 46340
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_22(self):
        num = 2500010000
        expected = 50000
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)

    def test_case_22(self):
        num = 2500090000
        expected = 50000
        output = Solution().mySqrt(num)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
