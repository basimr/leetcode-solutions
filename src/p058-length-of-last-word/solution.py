Space = " "


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        found_word = False
        word_length = 0

        for i in range(len(s) - 1, -1, -1):
            letter = s[i]
            if letter == Space:
                if found_word:
                    break
                else:
                    continue
            else:
                found_word = True
                word_length += 1

        return word_length
