class Solution:
    def getRow(self, n: int) -> List[List[int]]:
        a = []
        for i in range(n+1):
            a.append([0 for j in range(i+1)])
        
        for i in range(n+1):
            a[i][0], a[i][-1] = 1, 1

        for i in range(2,n+1):
            for j in range(1,i):
                a[i][j] = a[i-1][j-1] + a[i-1][j]
                
        return a[n]