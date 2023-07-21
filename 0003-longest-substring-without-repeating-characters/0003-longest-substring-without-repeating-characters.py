class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = res = 0
        for r in range(len(s)):
            while l < r and s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r-l+1)
        return res