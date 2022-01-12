class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix); n = len(matrix[0])
        
        t = 0; d = m-1; l = 0; r = n-1
        res = []
        
        while t <= d and l <= r:
            
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
            
            if l > r or t > d: break
                
            for i in range(t, d+1):
                res.append(matrix[i][r])
            r -= 1
            
            if l > r or t > d: break
            
            for i in range(r, l-1, -1):
                res.append(matrix[d][i])
            d -= 1
            
            if l > r or t > d: break
                
            for i in range(d, t-1, -1):
                res.append(matrix[i][l])
            l += 1
        
        return res
            