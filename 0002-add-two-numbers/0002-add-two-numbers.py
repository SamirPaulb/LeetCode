# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        cur = res
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = v1 + v2 + carry
            carry = v//10
            v = v % 10
            cur.next = ListNode(v)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return res.next