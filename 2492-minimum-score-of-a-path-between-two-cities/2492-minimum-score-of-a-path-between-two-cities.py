class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = {i:[] for i in range(1, n+1)}
        for a, b, d in roads:
            adj[a].append((b,d))
            adj[b].append((a,d))
        
        self.res = 2**31
        visited = {i:False for i in range(1, n+1)}
        def dfs(a):
            if visited[a]: return 
            visited[a] = True
            for b in adj[a]:
                self.res = min(self.res, b[1])
                dfs(b[0])
        
        dfs(1)
        return self.res