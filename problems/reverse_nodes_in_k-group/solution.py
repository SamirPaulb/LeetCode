# https://www.youtube.com/watch?v=Of0HPkk3JgI
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1: return head
        
        dummy = ListNode(-1)
        dummy.next = head
        
        pre, cur, nex = dummy, dummy, dummy
        
        count = 0
        while cur.next: # to find the length of linked list
            cur = cur.next
            count += 1
        
        while count >= k: # looping count/k number of times
            cur = pre.next
            nex = cur.next
            for i in range(k - 1): # for k nodes k - 1 links to be changed
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            count -= k
        
        return dummy.next
            