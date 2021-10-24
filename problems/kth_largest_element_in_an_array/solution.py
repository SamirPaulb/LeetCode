import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for i in nums:
            heapq.heappush(minHeap, i)
        
        arr = []
        while minHeap:
            arr.append(heapq.heappop(minHeap))
            
        return arr[-k]