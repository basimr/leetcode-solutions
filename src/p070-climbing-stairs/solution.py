def fibonacci(i: int) -> int:
    fib = [0, 1]
    while len(fib) < i+1:
        fib.append(fib[-1] + fib[-2])
    return fib[i]


class Solution:
    def climbStairs(self, n: int) -> int:
        return fibonacci(n+1)
