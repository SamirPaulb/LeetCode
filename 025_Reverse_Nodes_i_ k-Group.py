# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def reverseKGroup(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
class Solution(object):
    def reverseKGroup(self, head, k):
        if head is None:
            return None
        index = 0
        lead, last = 0, 0
        pos = head
        temp = ListNode(-1)
        temp.next = head
        head = temp
        start = head
        while pos is not None:
            if index % k == k - 1:
                last = pos.next
                start = self.reverseList(start, last)
                pos = start
            pos = pos.next
            index += 1
        return head.next

    def reverseList(self, head, end):
        pos = head.next
        last = end
        next_start = pos
        while pos != end:
            head.next = pos
            last_pos = pos
            pos = pos.next
            last_pos.next = last
            last = last_pos
        return next_start


