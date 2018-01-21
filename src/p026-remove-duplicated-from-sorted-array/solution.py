class Solution:
    @staticmethod
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        prev = 0
        curr = 1
        while curr < len(nums):
            if nums[prev] != nums[curr]:
                prev += 1
                nums[prev] = nums[curr]
            curr += 1
        return prev + 1
