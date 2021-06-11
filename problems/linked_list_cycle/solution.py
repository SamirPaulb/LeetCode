# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow  = head
        while (fast != None and fast.next != None and slow != None):
            fast =  fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    