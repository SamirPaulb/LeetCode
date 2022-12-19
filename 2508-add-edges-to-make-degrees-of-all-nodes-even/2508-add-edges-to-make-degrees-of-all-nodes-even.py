class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:set() for i in range(1, n+1)}
        for a, b in edges:
            adjList[a].add(b)
            adjList[b].add(a)
        
        oddedges = [node for node in adjList if len(adjList[node]) % 2]
        
        if len(oddedges) % 2 == 1: return False
        
        if len(oddedges) == 2:
            a, b = oddedges
            return True if any(a not in adjList[i] and b not in adjList[i] for i in adjList) else False
        
        if len(oddedges) == 4:
            a, b, c, d = oddedges
            # try connecting (a,b)and(b,c) or (a,c)and(b,d) or (a,d)and(b,c) 
            if a not in adjList[b] and c not in adjList[d]: return True
            if a not in adjList[c] and b not in adjList[d]: return True
            if a not in adjList[d] and b not in adjList[c]: return True
            return False
        
        return len(oddedges) == 0