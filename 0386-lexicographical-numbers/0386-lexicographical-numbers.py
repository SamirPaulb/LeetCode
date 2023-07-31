class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(start):
            arr = []
            for i in range(10):
                newStart = start*10 + i
                if newStart > n: break
                res.append(newStart)
                dfs(newStart)
        if n < 10: return range(1, n+1)
        for i in range(1, 10):
            res.append(i)
            dfs(i)
        
        return res