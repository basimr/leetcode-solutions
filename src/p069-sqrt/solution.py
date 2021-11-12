import math
import struct
from typing import List


N = 3


def estimate_root(x: int) -> int:
    """Produce a first guess of the square root for the Babylonian method.
        Here we derive our guess using half the digits of the squared number.
    """
    string = str(x)
    num_digits = len(str(x))

    if num_digits == 1:
        return x // 2
    if num_digits == 2:
        return x // 4

    half = math.ceil(num_digits / 2)
    half_of_x_digits = string[0:half]

    return int(half_of_x_digits)


def continue_guessing(history: List[int]) -> bool:
    if len(history) < N:
        return True

    last_n_estimates = history[-N:]
    for i, num in enumerate(last_n_estimates):
        if i == 0:
            pass
        if num != last_n_estimates[i-1]:
            return True

    return False


def fast_inverse_square_root(x: int) -> float:
    """Code copied from:
        https://github.com/ajcr/ajcr.github.io/blob/master/_posts/2016-04-01-fast-inverse-square-root-python.md
    """
    threehalfs = 1.5
    x2 = x * 0.5
    y = x

    packed_y = struct.pack('f', y)
    i = struct.unpack('i', packed_y)[0]  # treat float's bytes as int
    i = 0x5f3759df - (i >> 1)            # arithmetic with magic number
    packed_i = struct.pack('i', i)
    y = struct.unpack('f', packed_i)[0]  # treat int's bytes as float

    y = y * (threehalfs - (x2 * y * y))  # Newton's method
    y = y * (threehalfs - (x2 * y * y))  # Second iteration adds accuracy
    y = y * (threehalfs - (x2 * y * y))  # Third iteration adds even more accuracy to pass leetcode test cases
    return y


class Solution:
    @staticmethod
    def babylonian_method(x: int) -> int:
        """Calculate a square root using the Babylonian method."""
        if x == 0 or x == 1:
            return x

        x0 = estimate_root(x)
        history = [x0]
        xNext = x0

        while continue_guessing(history):
            xNext = 0.5 * (xNext + (x / xNext))
            truncated = math.floor(xNext)
            history.append(truncated)

        return history[-1]

    @staticmethod
    def doom_square_root(x: int) -> int:
        """Calculate square root using the Fast Inverse Square Root method used in Doom.
            Reference: https://en.wikipedia.org/wiki/Fast_inverse_square_root"""
        inverse_sqrt = fast_inverse_square_root(x)
        sqrt = 1 / inverse_sqrt
        truncated = math.floor(sqrt)
        return truncated

    # mySqrt = babylonian_method
    mySqrt = doom_square_root
