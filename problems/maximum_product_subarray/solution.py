class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        cs, ms = 1, nums[0]
        for i in nums:
            cs *= i
            ms = max(ms, cs)
            if cs == 0: cs = 1
        
        cs = 1
        for i in nums[::-1]:
            cs *= i
            ms = max(ms, cs)
            if cs == 0: cs = 1
                
        return ms