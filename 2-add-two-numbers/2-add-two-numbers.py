# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        node = res
        a = l1; b = l2; carry = 0
        while a or b or carry != 0:
            if a and b:
                v = a.val + b.val + carry
                carry = v // 10
                v = v % 10
                node.next = ListNode(v)
                node = node.next
                a = a.next
                b = b.next
            elif a and not b:
                v = a.val + carry
                carry = v // 10
                v = v % 10
                node.next = ListNode(v)
                node = node.next
                a = a.next
            elif not a and b:
                v = b.val + carry
                carry = v // 10
                v = v % 10
                node.next = ListNode(v)
                node = node.next
                b = b.next
            elif not a and not b and carry != 0:
                v = carry
                carry = 0
                node.next = ListNode(v)
                node = node.next
            
        return res.next