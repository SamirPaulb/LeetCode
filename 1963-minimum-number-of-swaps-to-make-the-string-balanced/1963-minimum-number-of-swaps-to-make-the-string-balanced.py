class Solution:
    def minSwaps(self, s: str) -> int:
        opn = 0
        for i in s:
            if i == '[':
                opn += 1
            if i == ']' and opn > 0:
                opn -= 1
        
        return (opn+1)//2