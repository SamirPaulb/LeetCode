class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for fr, to, pr in flights:
            adj[fr].append((pr, to))
        best_visited = [2**31] * n
        minHeap = [(0, -1, src)]
        while minHeap:
            pr, st, fr = heapq.heappop(minHeap)
            if st > k: continue
            if best_visited[fr] <= st: continue
            if fr == dst and st <= k: return pr
            best_visited[fr] = st
            for p, t in adj[fr]:
                heapq.heappush(minHeap, (pr+p, st+1, t))
        # print(best_visited)
        return -1