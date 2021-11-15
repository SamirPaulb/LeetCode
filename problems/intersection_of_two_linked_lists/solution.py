# https://www.youtube.com/watch?v=u4FWXfgS8jw&t=911s
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # take 2 dummy nodes a and b ; 
        a, b = headA, headB
        while a != b:
            if a == None: a = headB
            else: a = a.next
                
            if b == None: b = headA
            else: b = b.next
        
        return a