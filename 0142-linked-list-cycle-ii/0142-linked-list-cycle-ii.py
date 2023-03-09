# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        isCycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                isCycle = True
                break
        
        if not isCycle: return None
        while slow:
            if head == slow: return head
            head = head.next
            slow = slow.next
        