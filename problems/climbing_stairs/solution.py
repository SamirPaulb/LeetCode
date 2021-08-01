import math
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n==0:
            return 1 or 0
        ans = 0
        for i in range(n//2 + 1):
            m = n - i
            ans += math.factorial(m)/(math.factorial(m-i)*math.factorial(i))
        return int(ans)