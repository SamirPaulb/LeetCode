class Solution:
    def sortString(self, s: str) -> str:
        L = [0 for i in range(26)]
        for i in range(len(s)):
            a = ord(s[i] ) -97
            L[a] += 1
        
        st =""
        while len(st)< len(s):
            for i in range(26):
                if L[i] >0:
                    st += chr(i+97)
                    L[i] -= 1
            for i in range(25, -1, -1):
                if L[i] >0:
                    st += chr(i+97)
                    L[i] -= 1
                
                    
                
        
        return st
            
        
                