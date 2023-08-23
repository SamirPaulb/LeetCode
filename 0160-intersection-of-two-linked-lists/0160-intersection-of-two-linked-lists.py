# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA; b = headB
        cnt = 0
        while cnt < 3:
            if not a:
                a = headB
                cnt += 1
            if not b:
                b = headA
                cnt += 1
            if a == b: return a
            a = a.next
            b = b.next
        return None