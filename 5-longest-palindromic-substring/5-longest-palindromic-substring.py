class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if s == s[::-1] or n <= 1: return s
        p = 1
        res = s[0]
        
        for i in range(n):
            l = i; r = i
            while l>=0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length > p:
                    res = s[l:r+1]
                    p = length
                l -= 1
                r += 1
            
            l = i; r = i+1
            while l >=0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length > p:
                    res = s[l:r+1]
                    p = length
                l -= 1
                r += 1
                
        return res