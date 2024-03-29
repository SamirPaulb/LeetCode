class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        def dfs(path, u):
            if u == len(graph)-1: result.append(path + [u])
            else:
                for i in graph[u]: dfs(path + [u], i)
                    
        dfs([], 0)
        return result