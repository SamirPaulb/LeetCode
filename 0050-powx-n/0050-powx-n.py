class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = n
        if p < 0: p *= -1
        res = 1
        while p:
            if p%2 == 0:
                x = x * x 
                p //= 2
            else:
                res *= x
                p -= 1
        if n < 0: return 1/res
        return res