# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# Note:
# Given n will always be valid.
#
# Follow up:
# Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
class Solution(object):
    # def removeNthFromEnd(self, head, n):
    #     # with O(n) space
    #     index = []
    #     pos = head
    #     while pos is not None:
    #         index.append(pos)
    #         pos = pos.next
    #     ls = len(index)
    #     if n == ls:
    #         if ls > 1:
    #             return index[1]
    #         else:
    #             return None
    #     else:
    #         index_pos = ls - n - 1
    #         index[index_pos].next = index[index_pos + 1].next
    #         return head

    def removeNthFromEnd(self, head, n):
        # https://leetcode.com/discuss/86721/o-n-solution-in-java
        if head is None:
            return None
        slow = fast = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            head = head.next
            return head
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        curr = slow.next
        slow.next = curr.next
        return head
