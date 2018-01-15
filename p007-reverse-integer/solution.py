from math import floor, log

MAX_32_BIT_SIGNED_INTEGER = 2147483647
MIN_32_BIT_SIGNED_INTEGER = -2147483648


class Solution:
    @staticmethod
    def compute_num_digits(x):
        """Compute the number of digits in the given base-10 integer.
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 1
        num = abs(x)
        num_digits = int(floor(round(log(num, 10), 10))) + 1
        return num_digits

    @staticmethod
    def boundary_check(reversed_integer):
        """Return 0 if the integer exceeds the 32-bit signed integer limits,
        otherwise return the integer unchanged.
        :type reversed_integer: int
        :rtype: int
        """
        if reversed_integer < MIN_32_BIT_SIGNED_INTEGER \
                or reversed_integer > MAX_32_BIT_SIGNED_INTEGER:
            return 0
        else:
            return reversed_integer

    @staticmethod
    def reverse_via_string_manipulation(x):
        """Leetcode runtime: 98ms
        :type x: int
        :rtype: int
        """
        negative = (x < 0)
        num = abs(x)
        reversed_str = ''.join(reversed(str(num)))
        reversed_str.lstrip('0')
        reversed_int = int(reversed_str)
        reversed_int = -reversed_int if negative else reversed_int
        return Solution().boundary_check(reversed_int)

    @staticmethod
    def reverse_via_math_operations(x):
        """Leetcode runtime: 147ms
        :type x: int
        :rtype: int
        """
        num = abs(x)
        digits = Solution.compute_num_digits(num)
        reversed_int = 0
        for i in range(digits):
            ith_digit = num // (10**(digits-i-1))
            reversed_int += ith_digit * (10**i)
            num -= ith_digit * (10**(digits-i-1))
        reversed_int = -reversed_int if x < 0 else reversed_int
        return Solution().boundary_check(reversed_int)

    # reverse = reverse_via_string_manipulation
    reverse = reverse_via_math_operations
