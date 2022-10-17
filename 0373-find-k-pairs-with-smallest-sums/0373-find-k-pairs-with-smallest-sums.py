import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        for i in nums1:
            for j in nums2:
                s = i + j
                if len(heap) < k:
                    heapq.heappush(heap, [-s, i, j])
                else:
                    if s > - heap[0][0]: break
                    heapq.heappush(heap, [-s, i, j])
                    heapq.heappop(heap)
                    
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1:])
            
        return res[::-1]
    