class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        indices = []
        for i in range(len(nums)):
            if nums[i] == val:
                indices.append(i)
        removed = 0
        for i in indices:
            nums.pop(i - removed)
            removed += 1
        return len(nums)
