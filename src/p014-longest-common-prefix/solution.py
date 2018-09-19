class Solution:
    @staticmethod
    def longestCommonPrefix(strs):
        """Find the longest common prefix across a list of strings.
        This algorithm can match using the first string alone, making only one
        pass of the array, because the the longest common prefix must be part
        of that first string.

        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        first = strs[0]
        answer = len(first)
        for s in strs:
            matched = 0
            for i in range(min(len(first), len(s))):
                if first[i] == s[i]:
                    matched += 1
                else:
                    break
            answer = min(answer, matched)
            if answer == 0:
                break
        return first[:answer]
