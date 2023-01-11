class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((2*n + 1/4)**(1/2) - 1/2)
    