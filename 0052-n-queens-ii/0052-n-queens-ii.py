class Solution:
    def totalNQueens(self, n: int) -> int:
        col, posd, negd = set(), set(), set()
        self.res = 0
        
        def dfs(i):
            if i == n: 
                self.res += 1
                return
            for j in range(n):
                if j not in col and (i+j) not in posd and (i-j) not in negd:
                    col.add(j)
                    posd.add(i+j)
                    negd.add(i-j)
                    dfs(i+1)
                    col.remove(j)
                    posd.remove(i+j)
                    negd.remove(i-j)
        
        dfs(0)
        return self.res