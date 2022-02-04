class Solution(object):
    # def maximalSquare(self, matrix):
    #     """
    #     :type matrix: List[List[str]]
    #     :rtype: int
    #     """
    #     # Brute force O(mn^2)
    #     if matrix is None or len(matrix) == 0:
    #         return 0
    #     rows, cols = len(matrix), len(matrix[0])
    #     res = 0
    #     for i in range(rows):
    #         for j in range(cols):
    #             if matrix[i][j] == '1':
    #                 sqlen, flag = 1, True
    #                 while sqlen + i < rows and sqlen + j < cols and flag:
    #                     for k in range(j, sqlen + j + 1):
    #                         if matrix[i + sqlen][k] == '0':
    #                             flag = False
    #                             break
    #                     for k in range(i, sqlen + i + 1):
    #                         if matrix[k][j + sqlen] == '0':
    #                             flag = False
    #                             break
    #                     if flag:
    #                         sqlen += 1
    #                 if res < sqlen:
    #                     res = sqlen
    #     return res * res

    # def maximalSquare(self, matrix):
    #     # dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
    #     if matrix is None or len(matrix) == 0:
    #         return 0
    #     rows, cols, res = len(matrix), len(matrix[0]), 0
    #     dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    #     for i in range(1, rows + 1):
    #         for j in range(1, cols + 1):
    #             if matrix[i - 1][j - 1] == '1':
    #                 dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    #                 res = max(res, dp[i][j])
    #     return res * res

    def maximalSquare(self, matrix):
        # dp[j] = min([j], dp[j-1], prev) + 1
        # O(n) space
        if matrix is None or len(matrix) == 0:
            return 0
        rows, cols, res, prev = len(matrix), len(matrix[0]), 0, 0
        dp = [0] * (cols + 1)
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], dp[j], prev) + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return res * res

