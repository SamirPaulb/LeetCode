class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            k = ord(columnTitle[i]) - ord('A') + 1
            n = len(columnTitle) - i - 1
            res += k * 26**(n)
        return res