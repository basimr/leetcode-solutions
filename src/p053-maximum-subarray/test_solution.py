import unittest

from solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_example_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_example_2(self):
        nums = [1]
        expected = 1
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_example_3(self):
        nums = [5, 4, -1, 7, 8]
        expected = 23
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_1(self):
        nums = [-10]
        expected = -10
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_2(self):
        nums = [0]
        expected = 0
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_3(self):
        nums = [1, 2]
        expected = 3
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_4(self):
        nums = [-1, 2]
        expected = 2
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_5(self):
        nums = [-1, -2]
        expected = -1
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_6(self):
        nums = [-2, -1]
        expected = -1
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_7(self):
        nums = [0, 0]
        expected = 0
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_8(self):
        nums = [0, 100, 0]
        expected = 100
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_9(self):
        nums = [0, -100, 0]
        expected = 0
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_10(self):
        nums = [100, 0, 100]
        expected = 200
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_11(self):
        nums = [-100, 0, -100]
        expected = 0
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_12(self):
        nums = [200, -100, 900, -100, 300]
        expected = 1200
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_13(self):
        nums = [100, -100, 900, -100, 100]
        expected = 900
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_14(self):
        nums = [101, -100, 900, -100, 101]
        expected = 902
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)

    def test_case_15(self):
        nums = [-10, -15, -2, -17, -20]
        expected = -2
        output = Solution().maxSubArray(nums)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
