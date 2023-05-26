class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i:i for i in range(1, n+1)}
        
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a
    
        def union(a, b):
            pa = find(a)
            pb = find(b)
            parent[pb] = pa
        
        for a,b in edges:
            pa = find(a)
            pb = find(b)
            if pa == pb: return [a,b]
            union(a,b)
            
            