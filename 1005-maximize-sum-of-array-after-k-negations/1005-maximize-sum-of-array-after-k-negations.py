import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
        
        for i in range(k):
            a = heapq.heappop(heap)
            a *= -1
            heapq.heappush(heap, a)
        
        res = 0
        while heap:
            res += heapq.heappop(heap)
        
        return res