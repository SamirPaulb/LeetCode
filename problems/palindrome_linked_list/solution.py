# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a = ""
        s = head
        while s != None:
            a += str(s.val)
            s = s.next
        b = a[::-1]
        
        return a==b
        