from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        l = collections.Counter(s)
        r = collections.Counter()
        ans = 0
        for i in s:
            l[i] -= 1
            if l[i] == 0:
                del l[i]
            r[i] += 1
            if len(l) == len(r):
                ans += 1
        return ans