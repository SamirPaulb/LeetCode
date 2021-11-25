class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Implement Kadane's Algorithm
        cs, ms = nums[0], nums[0]   # Current Sum, Maximum Sum
        for i in range(1, len(nums)):
            cs = max(cs + nums[i], nums[i])
            ms = max(cs, ms)
        
        return ms
        