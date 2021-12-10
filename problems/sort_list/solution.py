# https://github.com/SamirPaul1/Problem-Solving/blob/main/Merge_Sort_on_LinkedList.py
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        middle = self.findMiddle(head)
        nextToMiddle = middle.next
        middle.next = None
        leftPart = self.sortList(head)
        rightPart = self.sortList(nextToMiddle)
        return self.sortMerge(leftPart, rightPart)
    
    def sortMerge(self, a, b):
        result = None
        if not a: return b
        if not b: return a
        if a.val <= b.val:
            result = a
            result.next = self.sortMerge(a.next, b)
        if a.val > b.val:
            result = b
            result.next = self.sortMerge(a, b.next)
        
        return result
    
    def findMiddle(self, head):
        if not head or not head.next: return head
        fast, slow = head.next, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        
        
        
        
        