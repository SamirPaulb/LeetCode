class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix); col = len(matrix[0])
        def check(num):
            n = 1
            for i in range(row):
                l, r = 0, col-1
                while l <= r:
                    m = l + (r-l)//2
                    if matrix[i][m] < num:
                        l = m + 1
                    else:
                        r = m - 1
                n += l
            return n <= k
        
        res = matrix[0][0]
        l,r = matrix[0][0], max(matrix[i][-1] for i in range(row))
        while l <= r:
            m = l + (r-l)//2
            if check(m):
                l = m+1
                res = m
            else:
                r = m-1
        return res