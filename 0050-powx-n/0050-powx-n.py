class Solution:
    def myPow(self, x: float, n: int) -> float:
        nNeg = False if n >= 0 else True
        xNeg = False if x >= 0 else True
        if nNeg: n *= -1
        res = 1
        while n:
            if n % 2 == 0:
                x *= x
                n /= 2
            else:
                res *= x
                n -= 1
        
        if xNeg and n%2: res *= -1
        if nNeg: res = 1/res
        return res