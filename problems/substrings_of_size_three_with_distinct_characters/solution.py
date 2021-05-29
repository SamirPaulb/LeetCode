class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-2):
            a = s[i] + s[i+1] + s[i+2]
            #print(a)
            if len(set(a)) ==3:
                sum += 1
        return sum
    
    