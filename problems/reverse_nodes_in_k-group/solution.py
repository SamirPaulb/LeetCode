class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1: return head
        
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur, nex = dummy, dummy, dummy
        
        count = 0
        while head:
            count += 1
            head = head.next
        
        while count >= k:
            cur = pre.next
            nex = cur.next
            for i in range(k - 1):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            count -= k
        
        return dummy.next
            