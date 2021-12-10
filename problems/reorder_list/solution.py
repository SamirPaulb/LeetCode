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
            b = b.next
            l += 1
            
            if not b: break
            
            b.val = arr[r]
            b = b.next
            r -= 1
        
        return head
        