class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i:[] for i in range(n)}
        for f, t, p in flights:
            adjList[f].append((t, p))
            
        visited = [2**31] * n
        minHeap = [(0, src, -1)]  # (price, source, no. of stops)
        res = 2**31
        while minHeap:
            price, stop, stopCount = heapq.heappop(minHeap)
        
            if stopCount > k: continue
            if stop == dst: return price
            
            if visited[stop] <= stopCount: continue
            visited[stop] = stopCount
            
            for t, p in adjList[stop]:
                heapq.heappush(minHeap, (price + p, t, stopCount + 1))
                    
        return -1