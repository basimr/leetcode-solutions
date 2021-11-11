from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums) - 1)

    def helper(self, nums: List[int], target: int, start: int, end: int):
        if start == end:
            if target <= nums[start]:
                return start
            else:
                return start + 1
        if target < nums[start]:
            return start
        if target > nums[end]:
            return end + 1

        mid_i = (start + end) // 2
        mid_num = nums[mid_i]

        if target < mid_num:
            return self.helper(nums, target, start, mid_i)
        elif target > mid_num:
            return self.helper(nums, target, mid_i + 1, end)
        else:
            return mid_i
