class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        for i in range(32):
            if x&(1<<i) != y&(1<<i):
                res += 1
        return res