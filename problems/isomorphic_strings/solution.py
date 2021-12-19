# https://www.youtube.com/watch?v=6Qkail843d8
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        for i in range(len(s)):
            if s[i] not in s2t: 
                s2t[s[i]] = t[i]
            else:
                if s2t[s[i]] != t[i]: return False
        
        t2s = {}
        for i in range(len(t)):
            if t[i] not in t2s:
                t2s[t[i]] = s[i]
            else:
                if t2s[t[i]] != s[i]: return False
        
        return True