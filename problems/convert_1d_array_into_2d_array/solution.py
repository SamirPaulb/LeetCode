class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = [[0]*n for i in range(m)]
        
        a = 0
        for i in range(m):
            for j in range(n):
                if a >= len(original): return []
                ans[i][j] = original[a]
                a += 1
        
        if a != len(original): return []
        return ans
        
