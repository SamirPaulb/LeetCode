class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        if n == 1: return [[1]]
        if n == 2: return [[1], [1,1]]
        res = [[1], [1,1]]
        for i in range(2, n):
            arr = res[-1]
            newarr = [1]
            for j in range(1, i):
                newarr.append(arr[j-1] + arr[j])
            newarr.append(1)
            res.append(newarr)
        
        return res
            