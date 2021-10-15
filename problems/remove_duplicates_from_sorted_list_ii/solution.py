# https://www.youtube.com/watch?v=7PGsMXlMzGA
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head
        
        dummy = ListNode(-1)
        itr = dummy 
        itr.next = head   # potential unique element
        cur = head.next
        
        while cur:
            isLoopRan = False
            while cur and itr.next.val == cur.val:
                isLoopRan = True
                cur = cur.next
                
            if isLoopRan: itr.next = cur
            else: itr = itr.next
            
            if cur: cur = cur.next
        
        return dummy.next