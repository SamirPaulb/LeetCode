class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l, rmax = 0, 0
        res = []
        lastInd = {ch:i for i, ch in enumerate(s)}
        for r in range(len(s)):
            rmax = max(rmax, lastInd[s[r]])
            if rmax == r:
                res.append(r-l+1)
                l = r+1
        return res