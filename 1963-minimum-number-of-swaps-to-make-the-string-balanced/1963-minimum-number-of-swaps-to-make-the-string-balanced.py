class Solution:
    def minSwaps(self, s: str) -> int:
        o = 0
        for i in s:
            if i == '[':
                o += 1
            else:
                if o > 0:
                    o -= 1
        
        if o in (0, 1): return o
        return (o+1)//2