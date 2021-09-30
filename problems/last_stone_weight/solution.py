class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st  = [-i for i in stones]
        heapq.heapify(st)
        while len(st) > 1:
            first = abs(heapq.heappop(st))
            second = abs(heapq.heappop(st))
            if first != second:
                heapq.heappush(st, -abs(first - second))
                
        if len(st) == 0: return 0
        
        return abs(st[0])