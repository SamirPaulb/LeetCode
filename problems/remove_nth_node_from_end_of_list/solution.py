class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow  = dummy, dummy
        for i in range(n):
            fast = fast.next
        
        if not fast: return None
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        tmp = slow.next.next
        slow.next = tmp
        
        return dummy.next
    
'''
TestCases:
[1,2,3,4,5]
2
[1]
1
[1,2]
1
[1,2]
2
'''