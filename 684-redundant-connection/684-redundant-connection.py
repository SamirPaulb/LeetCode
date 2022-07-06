class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = {i:i for i in range(1, n)}
        
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a
        
        def union(a, b):
            aRoot = find(a)
            bRoot = find(b)
            if aRoot == bRoot:
                return [a, b]
            else:
                parent[bRoot] = aRoot
        
        for a, b in edges:
            if union(a, b): return union(a, b)