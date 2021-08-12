# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode(-1)
        ans = l
        while l1 != None or l2 != None:
            if l1 != None and l2 != None and l1.val <= l2.val:
                l.next = l1
                l1 = l1.next
                l = l.next
            elif l1 != None and l2 != None and l1.val > l2.val:
                l.next = l2
                l2 = l2.next
                l = l.next
            elif l1 == None:
                l.next = l2
                l2 = l2.next
                l = l.next
            elif l2 == None:
                l.next = l1
                l1 = l1.next
                l = l.next
        return ans.next
            