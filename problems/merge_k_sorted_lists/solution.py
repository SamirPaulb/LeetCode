import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        myHeap = []
        
        for i in range(len(lists)):
            head = lists[i]
            a = head
            while a:
                myHeap.append(a.val)
                a = a.next
        # As heappush takes O(log(N)) time so First appending to the array (myHeap) then converting the array into a min heap so the time complexity will be O(N*N)  
        heapq.heapify(myHeap)
        
        arr = []
        
        while myHeap:
            arr.append(heapq.heappop(myHeap))
            
        newLL = ListNode(-1)
        a = newLL
        
        for i in arr:
            a.next = ListNode(i)
            a = a.next
            
        return newLL.next
                