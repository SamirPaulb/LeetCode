class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def helper(start):
            ans = []
            for aux in range(10):
                newStart = start * 10 + aux
                if newStart > n: 
                    break
                ans += [newStart]
                ans += helper(newStart)
            return ans
        
        if n < 10:
            return list([i for i in range(1, n+1)])
        
        res = []
        for i in range(1, 10):
            res += [i]
            res += helper(i)
        return res