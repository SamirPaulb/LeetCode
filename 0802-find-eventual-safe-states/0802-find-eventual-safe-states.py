class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        def dfs(node):
            if node in safe: 
                return safe[node]
            safe[node] = False
            for i in graph[node]:
                if not dfs(i):
                    return safe[i]
            safe[node] = True
            return True
        
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res