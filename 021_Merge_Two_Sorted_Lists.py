# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # dummy head
        pos = dummyHead = ListNode(-1)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                pos.next = l1
                l1 = l1.next
            else:
                pos.next = l2
                l2 = l2.next
            pos = pos.next
        # merge residual l1
        if l1 is not None:
            pos.next = l1
        # merge residual l2
        if l2 is not None:
            pos.next = l2
        return dummyHead.next


    # def mergeTwoLists(self, l1, l2):
    #     # recursive
    #     if l1 is None:
    #         return l2
    #     elif l2 is None:
    #         return l1
    #     if l1.val <= l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2

