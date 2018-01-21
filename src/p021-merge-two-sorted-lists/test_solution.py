import unittest

from .solution import Solution, ListNode


class SolutionTestCase(unittest.TestCase):
    def stringify_linked_list(self, l):
        string = ''
        while l:
            string += str(l.val)
            l = l.next
            if l:
                string += '→'
        return string

    def assert_equals_lists(self, a, b):
        self.assertEqual(
            self.stringify_linked_list(a),
            self.stringify_linked_list(b),
        )

    def test_simple_case(self):
        a = ListNode(2)
        b = ListNode(3)
        expected = ListNode(2, n=ListNode(3))
        output = Solution.mergeTwoLists(a, b)
        self.assert_equals_lists(expected, output)

    def test_empty_lists(self):
        a = None
        b = None
        expected = None
        output = Solution.mergeTwoLists(a, b)
        self.assert_equals_lists(expected, output)

    def test_first_list_empty(self):
        a = ListNode(5)
        b = None
        expected = ListNode(5)
        output = Solution.mergeTwoLists(a, b)
        self.assert_equals_lists(expected, output)

    def test_second_list_empty(self):
        a = None
        b = ListNode(5)
        expected = ListNode(5)
        output = Solution.mergeTwoLists(a, b)
        self.assert_equals_lists(expected, output)

    def test_equal_length_lists(self):
        a = ListNode(2, n=ListNode(5, n=ListNode(7)))
        b = ListNode(3, n=ListNode(8, n=ListNode(9)))
        expected = ListNode(2, n=ListNode(3, n=ListNode(5, n=ListNode(7, n=ListNode(8, n=ListNode(9))))))
        output = Solution.mergeTwoLists(a, b)
        self.assert_equals_lists(expected, output)

    def test_unequal_length_lists(self):
        a = ListNode(2, n=ListNode(5, n=ListNode(7)))
        b = ListNode(3, n=ListNode(8))
        expected = ListNode(2, n=ListNode(3, n=ListNode(5, n=ListNode(7, n=ListNode(8)))))
        output = Solution.mergeTwoLists(a, b)
        self.assert_equals_lists(expected, output)


if __name__ == '__main__':
    unittest.main()
