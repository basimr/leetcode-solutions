import unittest

from .solution import *


class SolutionTestCase(unittest.TestCase):
    def test_intToListNode_sanity(self):
        i1 = 342
        i2 = 465
        l1 = Solution.intToListNode(i1)
        l2 = Solution.intToListNode(i2)
        self.assertTrue(l1.val == 2 and l1.next.val == 4 and l1.next.next.val == 3)
        self.assertTrue(l2.val == 5 and l2.next.val == 6 and l2.next.next.val == 4)

    def test_intToListNode_zero(self):
        l = Solution.intToListNode(0)
        self.assertTrue(l.val == 0)
        self.assertTrue(l.next is None)

    def test_intToListNode_single_digit(self):
        l = Solution.intToListNode(5)
        self.assertTrue(l.val == 5)
        self.assertTrue(l.next is None)

    def test_intToListNode_number_ends_with_zero(self):
        l = Solution.intToListNode(10)
        self.assertTrue(l.val == 0)
        self.assertTrue(l.next.val == 1)
        self.assertTrue(l.next.next is None)
        l = Solution.intToListNode(100)
        self.assertTrue(l.val == 0)
        self.assertTrue(l.next.val == 0)
        self.assertTrue(l.next.next.val == 1)
        self.assertTrue(l.next.next.next is None)

    def test_listNodeToInt_sanity(self):
        l = ListNode(x=3)
        l.next = ListNode(x=2)
        l.next.next = ListNode(x=1)
        expected, actual = 123, Solution.listNodeToInt(l)
        self.assertEqual(expected, actual)

    def test_listNodeToInt_zero(self):
        l = ListNode(x=0)
        expected, actual = 0, Solution.listNodeToInt(l)
        self.assertEqual(expected, actual)

    def test_listNodeToInt_single_digit(self):
        l = ListNode(x=5)
        expected, actual = 5, Solution.listNodeToInt(l)
        self.assertEqual(expected, actual)

    def test_listNodeToInt_number_ends_with_zeroes(self):
        l = ListNode(x=0)
        l.next = ListNode(x=0)
        l.next.next = ListNode(x=1)
        expected, actual = 100, Solution.listNodeToInt(l)
        self.assertEqual(expected, actual)

    def test_addTwoNumbers_sanity(self):
        i1 = 342
        i2 = 465
        l1 = Solution.intToListNode(i1)
        l2 = Solution.intToListNode(i2)
        expected = Solution.intToListNode(807)
        actual = Solution.addTwoNumbers(l1, l2)
        self.assertEqual(expected, actual)

    def test_addTwoNumbers_zeroes(self):
        l1 = ListNode(x=0)
        l2 = ListNode(x=0)
        expected = ListNode(x=0)
        actual = Solution.addTwoNumbers(l1, l2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
