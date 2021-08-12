# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dn = ListNode(-1)
        dn.next = head
        a = dn
        while a.next != None:
            if a.next.val == val:
                a.next = a.next.next
            else:
                a = a.next
        return dn.next