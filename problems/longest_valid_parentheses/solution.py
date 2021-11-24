class Solution:
    def longestValidParentheses(self, s: str) -> int:
        o, c, ans = 0, 0, 0
        for i in s:
            if i == "(": o += 1
            if i == ")": c += 1
            if o == c: ans = max(ans, o + c)
            if c > o: o = c = 0
        o, c = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(": o += 1
            if s[i] == ")": c += 1
            if o == c: ans = max(ans, o + c)
            if o > c: o = c = 0
        
        return ans