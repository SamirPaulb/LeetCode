class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cs = 1  # Current So Far
        ms = nums[0] # Max So Far
        for i in nums:
            cs *= i
            ms = max(ms, cs)
            if cs == 0:
                cs = 1
        
        cs = 1
        for i in nums[::-1]:
            cs *= i
            ms = max(ms, cs)
            if cs == 0:
                cs = 1
        
        return ms