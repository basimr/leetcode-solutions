"""
Runtime: O(n log n)

Generate a randomized BST of the elements and their index,
then use it to query for complementary elements in log time.
"""
import random


class Node:
    def __init__(self, key, value=None):
        self.left = None
        self.right = None
        self.key = key
        self.value = value


class SimpleBST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key, value=None):
        new_node = Node(key, value)
        if not self.root:
            self.root = new_node
            return new_node
        curr = prev = self.root
        while curr:
            prev = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        if key < prev.key:
            prev.left = new_node
        else:
            prev.right = new_node
        return new_node

    def get(self, key, avoid_value=None):
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            elif curr.value == avoid_value:
                curr = curr.right
            else:
                return curr.value
        return None


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_with_indices = [(index, num) for index, num in enumerate(nums)]
        random.shuffle(nums_with_indices)

        tree = SimpleBST()
        for index, num in nums_with_indices:
            tree.insert(key=num, value=index)  # O(log n)

        for index, num in enumerate(nums):
            complement = target - num
            complement_index = tree.get(complement, avoid_value=index)  # O(log n)
            if complement_index is not None:
                return [index, complement_index]
