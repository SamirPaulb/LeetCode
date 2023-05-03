# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: return True
        slow, fast = head, head 
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        left = head
        pre = slow
        cur = pre.next
        nxt = cur.next
        while nxt:
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
            nxt = cur.next
        right = pre.next
        while right:
            if left.val != right.val: return False
            left = left.next
            right = right.next
        return True