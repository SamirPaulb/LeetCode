class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d: d[s[i]] += 1
            else: d[s[i]] = 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
        