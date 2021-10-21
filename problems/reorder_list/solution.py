# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        a = b = head
        while a:
            arr.append(a.val)
            a = a.next
        
        l, r = 0, len(arr) - 1
        
        while l <= r and b:
            b.val = arr[l]
            l += 1
            b = b.next
            if not b: break
            b.val = arr[r]
            r -= 1
            b = b.next
        
        return head