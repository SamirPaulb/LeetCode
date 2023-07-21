class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        res = 0
        tmp = ""
        while len(tmp) < len(b):
            tmp += a
            res += 1
        if b in tmp: return res
        if b in a+tmp: return res + 1
        return -1