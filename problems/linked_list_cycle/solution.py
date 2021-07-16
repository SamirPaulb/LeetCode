class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast != None and fast.next != None and slow != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
