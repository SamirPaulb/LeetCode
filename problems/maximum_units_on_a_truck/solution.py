class Solution:
    def maximumUnits(self, bt: List[List[int]], ts: int) -> int:
        m = [] # to store number Of Units Per Box
        for i in range(len(bt)):
            m.append(bt[i][1])
        ans = 0
        for i in range(len(bt)):
            me = max(m)     # max element of m 
            mi = m.index(me)    # index of max element (number Of Units Per Box)
            if bt[mi][0] < ts:
                ans += bt[mi][0] * bt[mi][1]
                m[mi] = 0
                ts -= bt[mi][0]
            elif bt[mi][0] >= ts:
                ans += bt[mi][1] * ts
                ts = 0
            
        return ans
        