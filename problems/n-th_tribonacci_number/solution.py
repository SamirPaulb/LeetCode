class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        a = 0
        b = 1
        c = 1
        i = 3
        while i <= n:
            tmp = a + b + c
            a = b
            b = c
            c = tmp
            i += 1
        return c