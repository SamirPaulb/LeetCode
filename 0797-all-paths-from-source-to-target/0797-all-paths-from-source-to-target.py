class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        adj = {i:graph[i] for i in range(len(graph))}
        visited = set()
        res = []
        def solve(i, path):
            if i == n-1:
                path.append(i)
                res.append(path)
                return 
            if i in visited: return 
            visited.add(i)
            for j in adj[i]:
                solve(j, path + [i])
            visited.remove(i)
        
        solve(0, [])
        return res