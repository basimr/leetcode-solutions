# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution:
    @staticmethod
    def mergeTwoLists(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2
        elif not l1 and not l2:
            return None
        elif l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        curr = head
        while l1 or l2:
            if l1 and not l2:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            elif l2 and not l1:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
            elif l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            elif l2.val <= l1.val:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        return head
