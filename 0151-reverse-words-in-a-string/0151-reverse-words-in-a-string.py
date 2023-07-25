class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        res = ''
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            else:
                j = i
                while j < len(s) and s[j] != ' ':
                    j += 1
                res = s[i:j] + ' ' + res 
                i = j if j > i else i+1
        
        return res[:-1]