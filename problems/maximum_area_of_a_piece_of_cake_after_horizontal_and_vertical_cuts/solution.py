class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.sort()
        vc.sort()
        maxh, maxv = max(hc[0], h - hc[-1]), max(vc[0], w - vc[-1])
        for i in range(len(hc)):
            maxh = max(maxh, hc[i] - hc[i-1])
        for i in range(len(vc)):
            maxv = max(maxv, vc[i] - vc[i-1])
        return (maxh * maxv) % 1000000007
