class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2: return l1 or l2
        if l1.val <= l2.val: a, b = l1, l2
        else: a, b = l2, l1
        res = a
        while a or b:
            if not a.next: 
                a.next = b
                return res
            elif not b: return res
            
            if a.next.val <= b.val: 
                a = a.next
            else:
                tmp = a.next
                a.next = b
                b = tmp
                a = a.next
        