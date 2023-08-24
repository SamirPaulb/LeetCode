class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = 0, 0
        l, r = 0, len(height)-1
        res = 0
        while l <= r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            if height[l] <= height[r]:
                res += min(lmax, rmax) - height[l]
                l += 1
            else:
                res += min(lmax, rmax) - height[r]
                r -= 1
        
        return res
