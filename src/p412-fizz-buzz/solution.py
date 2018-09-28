class Solution:
    def fizzBuzz(self, n):
        """This is fucking Fizz Buzz.
        :type n: int
        :rtype: List[str]
        """
        l = []
        for num in range(1, n + 1):
            if num % 3 == num % 5 == 0:
                l.append('FizzBuzz')
            elif num % 3 == 0:
                l.append('Fizz')
            elif num % 5 == 0:
                l.append('Buzz')
            else:
                l.append(str(num))
        return l
