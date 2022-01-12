class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for i in range(n)]
        
        t = 0; d = n-1; l = 0; r = n-1; v = 1
        while t <= d and l <= r:
            
            for i in range(l, r+1):
                mat[t][i] = v
                v += 1
            t += 1
            
            for i in range(t, d+1):
                mat[i][r] = v
                v += 1
            r -= 1
            
            if l > r or t > d: break
            
            for i in range(r, l-1, -1):
                mat[d][i] = v
                v += 1
            d -= 1
            
            for i in range(d, t-1, -1):
                mat[i][l] = v
                v += 1
            l += 1
        
        return mat