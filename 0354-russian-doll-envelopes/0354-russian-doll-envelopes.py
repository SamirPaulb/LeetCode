class Solution:
    def maxEnvelopes(self, env: List[List[int]]) -> int:
        env.sort(key = lambda x:(x[0], -x[1]))
        LIS = []
        for w, h in env:
            if not LIS or h > LIS[-1]:
                LIS.append(h)
            else:
                l,r = 0, len(LIS)
                while l <= r:
                    mid = l + (r - l)//2
                    if LIS[mid] < h:
                        l = mid + 1
                    else:
                        r = mid - 1
                LIS[l] = h
        
        return len(LIS)