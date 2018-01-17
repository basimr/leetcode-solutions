class Solution:
    @staticmethod
    def isPalindrome(x):
        """Leetcode runtime: 723ms
        :type x: int
        :rtype: bool
        """
        def recurse(num_str):
            if len(num_str) in [0, 1]:
                return True
            elif num_str[0] == num_str[-1]:
                return recurse(num_str[1:-1])
            else:
                return False

        if x < 0:
            return False
        else:
            string = str(x)
            return recurse(string)
