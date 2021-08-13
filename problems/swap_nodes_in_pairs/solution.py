# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        n1 = head
        n2 = n1.next
        head = n2
        while (True):
            temp = n2.next
            n2.next = n1
            if temp == None or temp.next == None:
                n1.next = temp
                break
            n1.next = temp.next
            n1 = temp
            n2 = temp.next
        return head