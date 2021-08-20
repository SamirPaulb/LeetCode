class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        al = {}
        for i in range(len(isConnected)):
            al[i] = []
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    al[i].append(j)
        #print(al)
        visited = [0]*len(al)
        q = []
        count = 0
        for i in al:
            if visited[i] == 1: continue
            q.append(i)
            count += 1
            while len(q) != 0:
                tmp = q.pop()
                if visited[tmp] == 1: continue
                visited[tmp] = 1
                if len(al[tmp]) != 0:
                    for j in al[tmp]:
                        if visited[j] == 1: continue
                        q.append(j)
        return count
                
            
            
                    
                        
            