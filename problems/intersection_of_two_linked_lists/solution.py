# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def get_len(node):
            n = 0
            while node != None:
                node = node.next
                n += 1
            return n
        
        lenA = get_len(headA)
        lenB = get_len(headB)
                
        for i in range(lenA - lenB):
            headA = headA.next
        
        for i in range(lenB - lenA):
            headB = headB.next  
            
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    