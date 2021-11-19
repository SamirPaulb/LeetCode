# Method - 2
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftBoundary, rightBoundary = [0] * n, [0] * n 
        lMax, rMax, ans = height[0], height[-1], 0
        
        for i in range(n):
            lMax = max(lMax, height[i])
            leftBoundary[i] = lMax
        
        for i in range(n - 1, -1, -1):
            rMax = max(rMax, height[i])
            rightBoundary[i] = rMax
        
        for i in range(n):
            ans += min(leftBoundary[i], rightBoundary[i]) - height[i]
        
        return ans