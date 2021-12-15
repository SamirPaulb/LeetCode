class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast: return True
            slow = slow.next
            fast = fast.next.next
        
        return False
    