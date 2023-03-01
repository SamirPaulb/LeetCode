class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = {i:(strs[i].count('0'), strs[i].count('1')) for i in range(len(strs))}
        dp = {}
        def dfs(i, m, n, tmp):
            if m<0 or n<0: 
                return -2**31
            if i >= len(strs):
                return 0
            if (i, m, n) in dp: return dp[(i, m, n)]
            z, o = count[i]
            if z <= m and o <= n:
                ans = max(1 + dfs(i+1, m-z, n-o, tmp+1), dfs(i+1, m, n, tmp))
            else:
                ans = dfs(i+1, m, n, tmp)
            dp[(i, m, n)] = ans
            return ans
        
        return dfs(0, m, n, 0)