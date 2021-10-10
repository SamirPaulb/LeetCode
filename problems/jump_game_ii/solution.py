# https://www.youtube.com/watch?v=dJ7sWiOoK7g
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        jumps = 0
        
        while r < len(nums) - 1:
            maxReachableIndex = 0
            for i in range(l, r+1):
                maxReachableIndex = max(maxReachableIndex, i + nums[i])
            
            l = r + 1
            r = maxReachableIndex
            jumps += 1
        
        return jumps