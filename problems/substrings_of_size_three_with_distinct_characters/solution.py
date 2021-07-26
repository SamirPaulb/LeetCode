class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        s = list(s)
        for i in range(len(s)-2):
            if len(set(s[i:i+3])) == 3:
                count += 1
                print(s[i:i+3])
        return count
    
    