class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hc = horizontalCuts
        if 0 not in hc: hc.append(0)
        if h not in hc: hc.append(h)
        hc.sort()
        
        vc = verticalCuts
        if 0 not in vc: vc.append(0)
        if w not in vc: vc.append(w)
        vc.sort()
        
        max_h = 0
        for i in range(1, len(hc)):
            max_h = max(max_h, hc[i] - hc[i-1])
        
        max_c = 0
        for i in range(1, len(vc)):
            max_c = max(max_c, vc[i] - vc[i-1])
        
        return (max_h * max_c) % (10**9 + 7)