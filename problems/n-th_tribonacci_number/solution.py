class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        i = 3
        while i <= n:
            tem = a + b + c
            a = b
            b = c 
            c = tem
            i += 1
        if n == 0:
            return 0
        return c