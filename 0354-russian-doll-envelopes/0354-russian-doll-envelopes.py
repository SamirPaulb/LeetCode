class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        LIS = []
        for (w, h) in envelopes:
            if not LIS or h > LIS[-1]:
                LIS.append(h)
            else:
                l, r = 0, len(LIS)
                while l < r:
                    m = l + (r - l) // 2
                    if LIS[m] < h:
                        l = m + 1
                    else:
                        r = m
                LIS[l] = h
                
        return len(LIS)
