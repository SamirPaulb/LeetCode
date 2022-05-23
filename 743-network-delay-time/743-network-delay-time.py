# https://leetcode.com/problems/network-delay-time/
# https://youtu.be/EaphyqKU4PQ
'''
# Implement Dijktra's Shortest Path Algorithm
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create Adjacency List 
        adjList = {i:[] for i in range(1, n+1)}
        for u, v, w in times:
            adjList[u].append((v, w))
        
        minHeap = [(0, k)]
        t = 0
        visited = set()
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited: continue
            visited.add(n1)
            t = max(t, w1)
            for n2, w2 in adjList[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return t if len(visited) == n else -1

# number of edges, e = len(times)
# n = total no. of nodes

# Time: O(e * log(n)) 
# Space: O(n)