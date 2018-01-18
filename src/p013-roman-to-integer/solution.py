ROMAN_TO_INT = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

class Solution:
    def recursive_roman_to_int(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        elif length == 1:
            return ROMAN_TO_INT[s]

        first, second = ROMAN_TO_INT[s[0]], ROMAN_TO_INT[s[1]]
        if first >= second:
            return first + self.romanToInt(s[1:])
        else:
            return (second - first) + self.romanToInt(s[2:])

    romanToInt = recursive_roman_to_int


