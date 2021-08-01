class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = ms = nums[0]
        for i in range(1, len(nums)):
            cs += nums[i]
            cs = max(cs, nums[i])
            ms = max(cs, ms)
        return ms
            