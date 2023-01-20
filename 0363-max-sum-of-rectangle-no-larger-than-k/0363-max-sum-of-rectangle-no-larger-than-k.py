class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix); col = len(matrix[0])
        res = -2**31
        for i in range(col):
            arr = [0] * row
            for j in range(i, col):
                sortedSum = [0]
                s = 0
                for r in range(row):
                    arr[r] += matrix[r][j]
                    s += arr[r]
                    idx = bisect.bisect_left(sortedSum, s-k)
                    if 0<= idx < len(sortedSum):
                        res = max(res, s - sortedSum[idx])
                    bisect.insort(sortedSum, s)
                        
                                            
        return res