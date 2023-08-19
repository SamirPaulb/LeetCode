class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = 0
        ms = nums[0]
        for num in nums:
            cs = max(cs+num, num)
            ms = max(ms, cs)
        
        return ms