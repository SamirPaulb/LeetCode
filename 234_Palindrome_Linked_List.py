# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def __init__(self):
    #     self.curr_head = None
    #
    # def isPalindrome(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     self.curr_head = head
    #     return self.check(head)
    #
    # def check(self, node):
    #     if node is None:
    #         return True
    #     isPal = self.check(node.next) and (self.curr_head.val == node.val)
    #     self.curr_head = self.curr_head.next
    #     return isPal

    def isPalindrome(self, head):
        # p2 is 2 times faster than p3
        # p1 and pre is used to reverse the first half of the list
        # so when the first while is over
        # p1 is in the middle
        # p3 is in middle + 1
        # p2 is in the end
        if head is None:
            return True
        p1, p2 = head, head
        p3, pre = p1.next, p1
        while p2.next is not None and p2.next.next is not None:
            p2 = p2.next.next
            pre = p1
            p1 = p3
            p3 = p3.next
            p1.next = pre
        if p2.next is None:
            p1 = p1.next

        while p3 is not None:
            if p1.val != p3.val:
                return False
            p1 = p1.next
            p3 = p3.next
        return True