class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2: return l1 or l2
        if l1.val < l2.val: a, b = l1, l2
        else: a, b = l2, l1
        ans = a
        while l1 or l2:
            if not a.next or not b: 
                a.next = b
                return ans
            elif a.next.val < b.val:
                a = a.next
            else:
                tmp = a.next
                a.next = b
                b = tmp
                a = a.next
        
        return ans
            