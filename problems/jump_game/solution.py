class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, reachable = 0, 0
        while i <= reachable:
            if reachable >= len(nums) - 1: return True
            reachable = max(reachable, i + nums[i])
            i += 1
        
        return False
    