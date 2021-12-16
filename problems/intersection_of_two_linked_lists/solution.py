# https://www.youtube.com/watch?v=u4FWXfgS8jw&t=911s
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        count = 0
        while a and b:
            if a == b:
                return a
                break
            a = a.next
            b = b.next
            if not a and b: 
                a = headB
                count += 1
            if not b and a: 
                b = headA
                count += 1
            
            if count > 2: return None
            
        return None
                
            