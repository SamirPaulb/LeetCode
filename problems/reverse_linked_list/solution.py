# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        c = head
        n = None
        p = None
        while c is not None:
            n = c.next
            c.next = p
            p = c
            c = n
        return p
    