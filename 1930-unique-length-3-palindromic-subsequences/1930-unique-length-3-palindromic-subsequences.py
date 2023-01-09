class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        elem_set = set(s)
        first_occur = {}
        for i in range(len(s)):
            if s[i] not in first_occur:
                first_occur[s[i]] = i
        
        last_occur = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in last_occur:
                last_occur[s[i]] = i
        
        res = 0
        for i in elem_set:
            l = first_occur[i]
            r = last_occur[i]
            if l + 1 <= r:
                res += len(set(s[l+1:r]))
        
        return res