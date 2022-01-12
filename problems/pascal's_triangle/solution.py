class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        res = [[1], [1,1]]
        
        for i in range(2, numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(res[i-1][j-1] + res[i-1][j])
            
            res.append(temp)
        
        return res