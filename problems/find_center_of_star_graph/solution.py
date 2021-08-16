class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = -2**31
        for i in range(len(edges)):
            a = max(edges[i])
            n = max(n, a)
        count = [0]*n
        for i in range(len(edges)):
            count[edges[i][0]-1] +=1 
            count[edges[i][1]-1] +=1  
        for i in range(len(count)):
            if count[i] == n-1:
                return i+1