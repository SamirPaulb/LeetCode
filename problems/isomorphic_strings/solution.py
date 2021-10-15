# https://www.youtube.com/watch?v=6Qkail843d8
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        
        for i, ch in enumerate(list(s)):
            if ch not in s2t:
                s2t[ch] = t[i]
            else:
                if s2t[ch] != t[i]: return False
        
        for i, ch in enumerate(list(t)):
            if ch not in t2s:
                t2s[ch] = s[i]
            else:
                if t2s[ch] != s[i]: return False
        
        return True