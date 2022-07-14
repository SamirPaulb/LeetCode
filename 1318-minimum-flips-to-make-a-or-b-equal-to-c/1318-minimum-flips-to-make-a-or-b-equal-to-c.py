class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            if (a & 1) | (b & 1) != (c & 1):
                if (c & 1) == 1:
                    res += 1
                else:
                    res += (a & 1) + (b & 1) 
            a, b, c = a>>1, b>>1, c>>1
        
        return res