class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        ans = 10
        tmp = 9
        for i in range(2, n+1):
            tmp *= (11 - i)
            ans += tmp
        return ans