import itertools
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
    @staticmethod
    def two_sum_via_exhaustive_search(nums, target):
        """Brute-force solution: check every possible pair of elements.
        Runs in O(n^2) time.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = range(len(nums))
        possibilities = itertools.combinations(indices, r=2)

        for i, j in possibilities:
            if nums[i] + nums[j] == target:
                return [i, j]

    @staticmethod
    def two_sum_via_binary_search(nums, target):
        """Generate a randomized BST of the elements and their index,
        then use it to query for complementary elements in log time.
        The elements are inserted into the tree in random order to
        yield an expected balanced tree. Runs in O(n log n) time.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_with_indices = [(index, num) for index, num in enumerate(nums)]
        random.shuffle(nums_with_indices)

        tree = SimpleBST()
        for index, num in nums_with_indices:
            tree.insert(key=num, value=index)

        for index, num in enumerate(nums):
            complement = target - num
            complement_index = tree.get(complement, avoid_value=index)
            if complement_index is not None:
                return [index, complement_index]

    @staticmethod
    def two_sum_via_hash_map(nums, target):
        """Create a hash map for each number and the indices in which
        it appears, then use it to query for a complementary number
        to one of the input numbers. Runs in O(n) time.
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

    # twoSum = two_sum_via_exhaustive_search
    # twoSum = two_sum_via_binary_search
    twoSum = two_sum_via_hash_map
