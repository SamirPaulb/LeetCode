class Solution:
    def minEatingSpeed(self, piles, h):
        def valid(speed):
            time = 0
            for num in piles:
                time += math.ceil(num/speed)
            return time <= h
        
        l, r, res = 1, sum(piles), sum(piles)
        while l <= r:
            mid = l + (r-l)//2
            if valid(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res