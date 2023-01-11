# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = l = ListNode(-1)
        right = r = ListNode(-1)
        cur = head
        while cur:
            if cur.val < x:
                l.next = ListNode(cur.val)
                l = l.next
            else:
                r.next = ListNode(cur.val)
                r = r.next
            cur = cur.next
        
        l.next = right.next
        return left.next
        