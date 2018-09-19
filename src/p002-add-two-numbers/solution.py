# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        this, that = self, other
        while True:
            if this is None and that is None:
                return True
            elif this is None or that is None:
                return False
            else:
                if this.val == that.val:
                    this, that = this.next, that.next
                else:
                    return False


class Solution:
    @staticmethod
    def listNodeToInt(l):
        if not l:
            return 0
        curr = l
        number = l.val
        place = 10
        while curr.next is not None:
            number += curr.next.val * place
            curr = curr.next
            place *= 10
        return number

    @staticmethod
    def intToListNode(i):
        if i < 0:
            raise Exception
        if i == 0:
            return ListNode(x=0)
        running = i
        head = curr = None
        while running != 0:
            digit = running % 10
            running -= digit
            running //= 10
            if not head:
                head = curr = ListNode(x=digit)
            else:
                curr.next = ListNode(x=digit)
                curr = curr.next
        return head

    @staticmethod
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        int1 = Solution.listNodeToInt(l1)
        int2 = Solution.listNodeToInt(l2)
        summation = int1 + int2
        return Solution.intToListNode(summation)
