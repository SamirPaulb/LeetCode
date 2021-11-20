class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0   # left, right pointer for scaning l to r for maxReachable index
        maxReachableIndex, jumps = 0, 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                maxReachableIndex = max(maxReachableIndex, i + nums[i])
            l = r + 1
            r = maxReachableIndex
            jumps += 1
        
        return jumps