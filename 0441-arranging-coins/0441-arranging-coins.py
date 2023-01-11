class Solution:
    def arrangeCoins(self, n: int) -> int:
        s = 1
        while s*(s+1)//2 <= n:
            s += 1
        return s-1