
class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        n = len(A)
        dp = [[0]*n for _ in range(n)]
        for length in range(n):
            index_i = 0
            for index_j in range(length, n):
                if index_j < index_i+2:
                    dp[index_i][index_j] = 0
                else:
                    dp[index_i][index_j] = float('inf')
                    for index_k in range(index_i+1, index_j):
                        val = dp[index_i][index_k] + dp[index_k][index_j] + (A[index_i]*A[index_k]*A[index_j])
                        dp[index_i][index_j] = min(dp[index_i][index_j], val)
                index_i += 1
        return dp[0][n-1]