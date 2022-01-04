class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadne's Algorithm
        cs = nums[0]
        ms = cs
        for i in range(1, len(nums)):
            cs += nums[i]
            cs = max(cs, nums[i])
            ms = max(ms, cs)
        
        return ms
    