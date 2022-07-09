class Solution:
    def maxPower(self, s: str) -> int:
        if not s: return 0
        sDict = {s[0]:1}
        res = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                sDict[s[i]] += 1
                res = max(res, sDict[s[i]])
            else:
                sDict[s[i]] = 1
        
        return res