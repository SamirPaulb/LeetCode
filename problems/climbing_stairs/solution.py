from math import factorial
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 0 or 1
        ans = 0
        for i in range(n//2 + 1):
            m = n - i
            ans += factorial(m)/(factorial(m-i)*factorial(i))
        return int(ans)