class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode(-1)
        pre.next = head
        ans = pre
        a = pre.next
        while a and a.next:
            isLoopRan = False
            while a.next and a.val == a.next.val:
                a = a.next
                isLoopRan = True
                
            if isLoopRan: # nodeCount[0] occurs more than one times
                tmp = a.next
                a.next = None
                pre.next = tmp
                a = tmp
            else:
                a = a.next
                pre = pre.next
        
        return ans.next