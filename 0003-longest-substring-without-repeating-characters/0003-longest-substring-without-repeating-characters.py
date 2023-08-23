class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        taken = set()
        l = res = 0
        for r in range(len(s)):
            while s[r] in taken and l < r:
                taken.remove(s[l])
                l += 1
            res = max(res, r-l+1)
            taken.add(s[r])
        return res