class Solution:
    def replaceDigits(self, s: str) -> str:
        
        def shift(ch, n):
            return chr(ord(ch)+n)
        
        if(len(s) == 1):
            return s
        
        result = ''
        for i in range(len(s)):
            if(i % 2 == 0):
                result += s[i]
            else:
                result += shift(s[i-1], int(s[i]))
        return result
        
    
        