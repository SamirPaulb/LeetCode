class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        res = 1
        tmp = a
        while len(tmp) < len(b):
            tmp += a
            res += 1
        if b in tmp: return res
        tmp += a
        return res+1 if b in tmp else -1