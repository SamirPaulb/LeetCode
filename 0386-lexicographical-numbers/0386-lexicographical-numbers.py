class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def helper(start):
            tmp = []
            for i in range(10):
                num = start*10 + i
                if num > n:
                    break
                tmp += [num]
                tmp += helper(num)
            return tmp
        
        if n < 10: return list(range(1, n+1))

        res = []
        for i in range(1, 10):
            if i > n: break
            res += [i]
            res += helper(i)
        
        return res