class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2: return l1 or l2
        if l1.val < l2.val: a, b = l1, l2
        else: a, b = l2, l1
        ans = a
        while a and b:
            if not a.next and b: 
                a.next = b
                break
            if not b: break
            if a.next.val > b.val:
                tmp = a.next
                a.next = b
                b = tmp
                a = a.next
            else:
                a = a.next
        
        return ans
        
        
        
        
        
        