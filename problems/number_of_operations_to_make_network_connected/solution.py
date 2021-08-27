# reference:    https://www.youtube.com/watch?v=3JIwIRir2sM

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        al = {}  #Adjacency List
        for i in range(n):
            al[i] = []
        edge_count = 0
        for i in connections:
            al[i[0]].append(i[1])
            al[i[1]].append(i[0])
            edge_count += 1
        #print(al)
        #print(edge_count)
        #Find Number of not connected components by using DFS or by the concept of number of provinces question   https://leetcode.com/problems/number-of-provinces/
        visited = [False]*n
        q = []
        components = 0
        for i in al:
            if visited[i]: continue
            q.append(i)
            components += 1
            while len(q) != 0:
                tmp = q.pop()
                if visited[tmp]: continue
                visited[tmp] = True
                if len(al[tmp]) != 0:
                    for j in al[tmp]:
                        if visited[j]: continue
                        q.append(j)
        #print(components) --> number of provinces
        if edge_count < n-1:
            return -1
        
        reduntant = edge_count - ((n-1) - (components-1)) # number of extra edges

        if reduntant >= (components-1):
            return (components-1)
        return -1
            
            
            
            
            
            
                