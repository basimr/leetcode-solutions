class Solution:
    @staticmethod
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif not stack:
                return False
            elif (c == ')' and stack[-1] == '(') \
                    or (c == '}' and stack[-1] == '{') \
                    or (c == ']' and stack[-1] == '['):
                stack.pop()
                continue
            else:
                return False
        return False if stack else True
