"""
Runtime: O(n^2)

Brute-force solution: check every possible pair of elements.
"""

import itertools


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = range(len(nums))
        possibilities = itertools.combinations(indices, r=2)

        for i, j in possibilities:
            if nums[i] + nums[j] == target:
                return [i, j]
