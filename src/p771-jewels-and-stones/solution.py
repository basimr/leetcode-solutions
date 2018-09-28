class Solution:
    def numJewelsInStones(self, jewels, stones):
        """Count the number of jewels present in a string of stones.
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counts = {}
        for s in stones:
            count = counts.get(s, 0)
            counts[s] = count + 1

        num_jewels = 0
        for j in jewels:
            num_jewels += counts.get(j, 0)

        return num_jewels
