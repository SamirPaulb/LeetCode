class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1+4*n*2)**(1/2))//2)