class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def lcs(A, B):
            n, m = len(A)+1, len(B)+1
            dp = [["" for _ in range(m)] for _ in range(n)]
            for index_i in range(1, n):
                for index_j in range(1, m):
                    if A[index_i-1] == B[index_j-1]:
                        dp[index_i][index_j] = dp[index_i-1][index_j-1] + A[index_i - 1]
                    else:
                        dp[index_i][index_j] = max(dp[index_i-1][index_j], dp[index_i][index_j-1], key=len)
            return dp[-1][-1]
        
        result = ""
        index_i, index_j = 0, 0
        for s in lcs(str1, str2):
            while str1[index_i] != s:
                result += str1[index_i]
                index_i += 1
            while str2[index_j] != s:
                result += str2[index_j]
                index_j += 1
                
            result += s
            index_i, index_j = index_i+1, index_j+1
            
        return result + str1[index_i:] + str2[index_j:]