# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return None
        slow, fast = head, head.next
        isCycle = False
        while fast and fast.next:
            if slow == fast: 
                isCycle = True
                break
            slow = slow.next
            fast = fast.next.next
        
        if isCycle == False: return None
        
        slow, fast = head, fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
    