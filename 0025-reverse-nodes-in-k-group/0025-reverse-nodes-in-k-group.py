# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        n = 0; cur = head
        while cur: cur = cur.next; n += 1

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        
        for i in range(n//k):
            cur = pre.next
            nex = cur.next
            for j in range(k-1):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
        
        return dummy.next
