# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        
        s2 = ""
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        
        res = ListNode(-1)
        cur = res
        s = str(int(s1) + int(s2))
        for i in s:
            cur.next = ListNode(int(i))
            cur = cur.next
        
        return res.next