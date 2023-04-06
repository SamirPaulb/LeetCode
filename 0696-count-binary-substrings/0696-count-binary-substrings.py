class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        p, n, res = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                n += 1
            else:
                res += min(p, n)
                p = n
                n = 1
        
        res += min(p, n)
        return res