class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        res = 0
        
        while a > 0:
            res += a & 1
            a = a >> 1
            
        return res