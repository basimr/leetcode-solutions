import math
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

    mySqrt = babylonian_method
