class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_possible = len(set(s))
        longest = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                char = s[j]
                if char not in seen:
                    seen.add(char)
                else:
                    break
                longest = len(seen) if len(seen) > longest else longest
                if longest > (len(s) - i) or longest == max_possible:
                    return longest
        return longest
