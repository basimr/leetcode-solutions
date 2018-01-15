"""
Runtime: O(n)

Create a hash map for each numbers and the indices in which
it appears, then use it to query for a complementary value
to one of the input numbers.
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = {}
        for index, num in enumerate(nums):
            num_indices = indices.get(num)
            if num_indices is None:
                indices[num] = [index]
            else:
                num_indices.append(index)

        for index, num in enumerate(nums):
            complement = target - num
            complement_indices = indices.get(complement)
            if complement_indices is None:
                continue
            elif num != complement:
                complement_index = complement_indices[0]
                return [index, complement_index]
            elif num == complement and len(complement_indices) > 1:
                return complement_indices[0:2]
            else:
                continue
