class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True
        
        def isPalindrome(s):
            return s == s[::-1]
        
        l = 0; r = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
        
        