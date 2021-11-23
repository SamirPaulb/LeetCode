class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, maxReachable = 0, 0
        while i <= maxReachable:
            if maxReachable >= len(nums) - 1: return True
            maxReachable = max(maxReachable, i + nums[i])
            i += 1
        
        return False