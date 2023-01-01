class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        s = list(s.split(' '))
        if len(s) != len(p): return False
        sd = {}
        for i, ch in enumerate(p):
            if ch not in sd:
                sd[ch] = {s[i]}
            else:
                sd[ch].add(s[i])
                
        for ch in sd:
            if len(sd[ch]) != 1: return False
        
        pd = {}
        for i, ch in enumerate(s):
            if ch not in pd:
                pd[ch] = {p[i]}
            else:
                pd[ch].add(p[i])
        
        for ch in pd:
            if len(pd[ch]) != 1: return False
        
        return True
                