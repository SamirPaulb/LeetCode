class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lb = [0]*n
        lmax = 0
        for i in range(n):
            lmax = max(lmax, height[i])
            lb[i] = lmax
        rb = [n-1]*n
        rmax = 0
        for i in range(n-1, -1, -1):
            rmax = max(rmax, height[i])
            rb[i] = rmax
        res = 0
        for i in range(n):
            res += min(lb[i], rb[i]) - height[i]
        return res