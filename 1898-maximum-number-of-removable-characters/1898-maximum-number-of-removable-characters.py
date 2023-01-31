class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(s, p, arr):
            arr = set(arr)
            i = j = 0
            while i < len(s) and j < len(p):
                if s[i] == p[j] and i not in arr:
                    j += 1
                i += 1
            return j == len(p)
        
        res = 0
        l, r = 0, len(removable)-1
        while l <= r:
            mid = l + (r - l)//2
            if isSubsequence(s, p, removable[:mid+1]):
                res = max(res, mid+1)
                l = mid + 1
            else:
                r = mid - 1
        
        return res