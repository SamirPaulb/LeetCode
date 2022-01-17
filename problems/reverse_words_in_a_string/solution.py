# https://www.youtube.com/watch?v=vhnRAaJybpA
class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0; j = 0; n = len(s); res = ""
        
        while i < n:
            if s[i] == " ":
                i += 1
            else:
                j = i
                
                while j < n and s[j] != " ":
                    j += 1
                    
                subStr = s[i:j]
                
                if res == "": 
                    res = subStr
                else:
                    res = subStr + " " + res
                
                i = j
        
        return res