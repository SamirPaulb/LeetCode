class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        firstRemovedIndexFromLeft = [0]*len(s)
        firstRemovedIndexFromRight = [len(s)-1]*len(s)
        l = 0
        for i in range(len(s)):
            if s[i] == t[l]:
                l += 1
            firstRemovedIndexFromLeft[i] = l
            if l == len(t): return 0
            
        res, r = len(t), len(t)-1
        for i in range(len(s)-1, -1, -1):
            l = firstRemovedIndexFromLeft[i]
            if l <= r:
                res = min(res, r-l+1)
            if s[i] == t[r]:
                r -= 1
            res = min(res, r+1)
        
        return res