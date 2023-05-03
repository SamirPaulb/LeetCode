# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = pre.next 
        nxt = cur.next
        while nxt:
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
            nxt = cur.next
        return dummy.next