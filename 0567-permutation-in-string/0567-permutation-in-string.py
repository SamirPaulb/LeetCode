class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1d = collections.Counter(s1)
        for i in range(k-1, len(s2)):
            sb = s2[i-k+1:i+1]
            sbd = collections.Counter(sb)
            if sbd == s1d: return True
        
        return False