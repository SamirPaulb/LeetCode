# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s = ""
        while head != None:
            s += str(head.val)
            head = head.next
        a = s[::-1]
        print(s)
        return a == s