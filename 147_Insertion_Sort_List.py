# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # https://discuss.leetcode.com/topic/8570/an-easy-and-clear-way-to-sort-o-1-space
        if head is None:
            return None
        helper = ListNode(-1000)
        pre, curr = helper, head
        while curr is not None:
            next_step = curr.next
            while pre.next and pre.next.val < curr.val:
                pre = pre.next
            curr.next = pre.next
            pre.next = curr
            pre = helper
            curr = next_step
        return helper.next
