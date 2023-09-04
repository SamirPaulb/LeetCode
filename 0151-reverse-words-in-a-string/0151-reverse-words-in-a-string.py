class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        i = len(s)-1
        while i >= 0:
            tmp = ''
            while i >= 0 and s[i] != ' ':
                tmp += s[i]
                i -= 1
            else:
                i -= 1
            if tmp:
                res += tmp[::-1] + ' '
        
        return res[:-1]