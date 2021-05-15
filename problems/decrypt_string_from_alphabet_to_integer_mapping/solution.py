class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        resultStr = ""
        while i <len(s):
            if i+2 < len(s):
                if s[i+2] == "#":
                    resultStr += chr(int(s[i]+s[i+1])+96)
                    i = i+3
                else:
                    resultStr += chr(int(s[i])+96)
                    i = i + 1
                
            else:
                resultStr += chr(int(s[i])+96)
                i = i + 1
        return resultStr
            
        