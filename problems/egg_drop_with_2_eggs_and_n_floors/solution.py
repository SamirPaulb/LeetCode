class Solution:
    def twoEggDrop(self, n: int) -> int:
        c = 0
        i = 0
        while i < n:
            c += 1
            i += c
        return c
            
            
            