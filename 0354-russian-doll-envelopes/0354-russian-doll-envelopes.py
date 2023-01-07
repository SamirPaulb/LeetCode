class Solution:
    def maxEnvelopes(self, env: List[List[int]]) -> int:
        env.sort(key = lambda x:(x[0], -x[1]))
        LIS = []
        for w, h in env:
            if not LIS or h > LIS[-1]:
                LIS.append(h)
            else:
                left = bisect.bisect_left(LIS, h)
                LIS[left] = h
        
        return len(LIS)