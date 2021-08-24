class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        m,n=len(grid),len(grid[0])
        k=k%(m*n)
        for i in grid:
            for j in i:
                res.append(j)
        res=res[m*n-k:]+res[0:m*n-k]
        cp=n
        aux=[]
        ans=[]
        for i in res:
            aux.append(i)
            cp-=1
            if cp==0:
                ans.append(aux)
                aux=[]
                cp=n
        return ans
                