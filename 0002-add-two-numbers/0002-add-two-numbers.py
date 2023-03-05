# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        n1 = self.getLen(l1); n2 = self.getLen(l2)
        if n1 >= n2:
            return self.solve(l1, l2)
        return self.solve(l2, l1)
    
    
    
    
    def solve(self, l1, l2):
        head = prev = l1
        carry = 0
        while l1:
            v = l1.val + carry
            v += l2.val if l2 else 0
            carry = v // 10
            v = v % 10
            l1.val = v
            prev = l1
            l1 = l1.next
            if l2: l2 = l2.next
        if carry:
            prev.next = ListNode(carry)
        return head
        
        
    def getLen(self, head):
        n = 0
        while head:
            n += 1
            head = head.next
        return n