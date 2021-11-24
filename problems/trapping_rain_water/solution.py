class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, lMax, rMax, ans = 0, len(height) - 1, height[0], height[-1], 0
        while l <= r:
            if height[l] <= height[r]:
                lMax = max(lMax, height[l])
                ans += lMax - height[l]
                l += 1
            else:
                rMax = max(rMax, height[r])
                ans += rMax - height[r]
                r -= 1
        
        return ans