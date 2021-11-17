# https://github.com/SamirPaul1/Problem-Solving/blob/main/Merge%20Sort%20on%20LinkedList.py
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        middle = self.findMiddle(head)
        nextToMiddle = middle.next
        middle.next = None
        leftPart = self.sortList(head)
        rightPart = self.sortList(nextToMiddle)
        return self.mergeSort(leftPart, rightPart)    
    
    def mergeSort(self, a, b):
        if not a or not b: return a or b
        if a.val <= b.val:
            result = a
            result.next = self.mergeSort(a.next, b)
        else:
            result = b
            result.next = self.mergeSort(a, b.next)
        return result
        
    def findMiddle(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        
        