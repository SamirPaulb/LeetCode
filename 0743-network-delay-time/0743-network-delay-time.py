class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}
        for u,v,w in times:
            adj[u].append((v,w))
            
        minHeap = [(0, k)]
        visited = set()
        res = 0
        while minHeap:
            w, v = heapq.heappop(minHeap)
            if v in visited: continue
            visited.add(v)
            res = max(res, w)
            for v1, w1 in adj[v]:
                heapq.heappush(minHeap, (w+w1, v1))
        
        return res if len(visited) == n else -1