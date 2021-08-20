class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if [start, end] in edges or [end, start] in edges or n == 1:
            return True
        al = {}
        for i in range(n):
            al[i] = []
        for i in edges:
            al[i[0]].append(i[1])
            al[i[1]].append(i[0])
        #print(al)
        visited = [0]*n
        q = []
        
        q.append(start)
        while len(q) != 0:
            tmp = q.pop()
            if visited[tmp] == 1: continue
            visited[tmp] = 1
            if len(al[tmp]) != 0:
                for j in al[tmp]:
                    if j == end: return True
                    if visited[j] == 1: continue
                    q.append(j)
                        
        return False
                    
                    
                    
                    
                    
                    
                    
       