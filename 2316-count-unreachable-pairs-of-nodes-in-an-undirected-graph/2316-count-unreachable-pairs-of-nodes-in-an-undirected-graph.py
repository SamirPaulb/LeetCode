class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        unreachable = []
        for a in range(n):
            if a in visited: continue
            q = collections.deque([a])
            length = 0
            while q:
                a = q.popleft()
                if a in visited: continue
                visited.add(a)
                length += 1
                for b in adj[a]:
                    if b in visited: continue
                    q.append(b)
            unreachable.append(length)
        
        s = 0
        res = 0
        for i in unreachable:
            res += s * i
            s += i
        return res
        
    
    
# [1, 2, 4]