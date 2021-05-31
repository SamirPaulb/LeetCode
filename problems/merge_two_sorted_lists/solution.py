# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = ListNode(-1)
        temp = s
        while (l1 != None) and (l2 != None) :
            if l1.val<= l2.val:
                temp.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1 != None:
            temp.next = l1
        elif l2 != None:
            temp.next = l2
        
        return s.next
        