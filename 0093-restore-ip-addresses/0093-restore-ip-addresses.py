class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(i, k, tmp):
            # print(tmp)
            if k >= 4 or i >= len(s):
                if i == len(s) and k == 4:
                    res.append(tmp[:-1])
                return
            
            if s[i] == '0':
                dfs(i+1, k+1, tmp + s[i] + '.')
            else:
                if i < len(s):
                    dfs(i+1, k+1, tmp + s[i] + '.')
                if i+1 <= len(s): 
                    dfs(i+2, k+1, tmp + s[i:i+2] + '.')
                if i+2 <= len(s) and s[i:i+3] <= '255': 
                    dfs(i+3, k+1, tmp + s[i:i+3] + '.')
        
        dfs(0, 0, "")
        return res