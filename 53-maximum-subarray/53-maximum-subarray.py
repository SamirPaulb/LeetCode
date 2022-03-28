class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kaden's Algorithms
        cs = nums[0]
        ms = nums[0]
        
        for i in nums[1:]:
            cs += i
            cs = max(cs, i)
            ms = max(ms, cs)
        
        return ms