import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        myHeap = []
        for head in lists:
            while head:
                myHeap.append(head.val)
                head = head.next
                
        heapq.heapify(myHeap)
        
        ans = ListNode(-1)
        a = ans
        
        while myHeap:
            a.next = ListNode(heapq.heappop(myHeap))
            a = a.next
        
        return ans.next