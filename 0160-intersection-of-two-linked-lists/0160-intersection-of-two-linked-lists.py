# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cnt = 0
        ha, hb = headA, headB
        while ha and hb:
            if ha == hb: return ha
            ha = ha.next
            hb = hb.next
            if not ha: 
                cnt += 1
                ha = headB
            if not hb: 
                hb = headA
                cnt += 1
            if cnt > 2: return 
        