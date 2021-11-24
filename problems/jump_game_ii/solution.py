class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0   #left, right pointer for scaning l to r for maxReachable index
        maxReachable, jumps = 0, 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                maxReachable = max(maxReachable, i + nums[i])
            l = r + 1
            r = maxReachable
            jumps += 1
        
        return jumps