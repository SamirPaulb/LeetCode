class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        @lru_cache(None)
        def dfs(i, j, k):
            if i >= n and j >= m: return True
            if i < n and s1[i] == s3[k] and dfs(i + 1, j, k + 1): return True
            if j < m and s2[j] == s3[k] and dfs(i, j + 1, k + 1): return True
            return False
        
        return Counter(s1) + Counter(s2) == Counter(s3) and dfs(0, 0, 0)
        