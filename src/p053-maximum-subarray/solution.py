import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -math.inf
        curr_sum = 0
        for num in nums:
            curr_sum = max(num, curr_sum+num)
            best_sum = max(curr_sum, best_sum)
        return best_sum
