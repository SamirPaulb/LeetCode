class Solution(object):
    # def minCut(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     # https://discuss.leetcode.com/topic/2840/my-solution-does-not-need-a-table-for-palindrome-is-it-right-it-uses-only-o-n-space
        ls = len(s)
        cut = [i -1 for i in range(ls + 1)]
        for i in range(ls):
            # odd length
            pos = 0
            while i - pos >= 0 and i + pos < ls and s[i - pos] == s[i + pos]:
                cut[i + pos + 1] = min(cut[i + pos + 1], 1 + cut[i - pos])
                pos += 1
            # even length
            pos = 1
            while i - pos + 1 >= 0 and i + pos < ls and s[i - pos + 1] == s[i + pos]:
                cut[i + pos + 1] = min(cut[i + pos + 1], 1 + cut[i - pos + 1])
                pos += 1
        return cut[ls]

    # def minCut(self, s):
    #     if len(s) <= 1:
    #         return 0
    #     ls = len(s)
    #     d = [0] * ls
    #     pal = [[False] * ls for _ in range(ls)]
    #     for i in range(ls - 1, -1, -1):
    #         d[i] = ls - i - 1
    #         for j in range(i, ls):
    #             if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
    #                 pal[i][j] = True
    #                 if j == ls - 1:
    #                     d[i] = 0
    #                 elif d[j + 1] + 1 < d[i]:
    #                     d[i] = d[j + 1] + 1
    #     return d[0]