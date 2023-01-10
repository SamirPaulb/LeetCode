class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(o, c, tmp):
            if c > o: return
            if o == c == n:
                res.append(tmp)
                return
            if o > c:
                dfs(o, c+1, tmp + ')')
            if o < n: 
                dfs(o+1, c, tmp + '(')
        
        dfs(0, 0, "")
        return res