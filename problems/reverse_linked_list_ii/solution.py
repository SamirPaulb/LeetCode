# using a for loop concept of https://leetcode.com/problems/reverse-nodes-in-k-group/
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy = ListNode(-1) # creating dummy node if by chance left == head
        dummy.next = head
        
        if left == right: return dummy.next # left and right are in same node in the LinkedList
        
        pre = dummy
        cur = pre.next
        nex = cur.next
        
        # Move these three pointers to left
        n = 1
        while n < left:
            pre = pre.next
            cur = cur.next
            nex = nex.next
            n += 1
        
        # Now play with link pointers and reverse
        for i in range(right - left):
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        
        return dummy.next
    
    
    
''' Test Cases:
[1,2,3,4,5]
2
4
[5]
1
1
[3,5]
1
1
[3,5]
2
2
[3,5]
1
2
'''
            