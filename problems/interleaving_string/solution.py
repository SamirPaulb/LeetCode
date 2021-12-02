class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        @lru_cache(None)
        
        def dfs(i, j, k):
            if i > m - 1 and j > n - 1:
                return True
            if i < m and s1[i] == s3[k] and dfs(i + 1, j, k + 1):
                return True
            if j < n and s2[j]  == s3[k] and dfs(i, j + 1, k + 1):
                return True
            return False
        
        return Counter(s1) + Counter(s2) == Counter(s3) and dfs(0, 0, 0)