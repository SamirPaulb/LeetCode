class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        for i in range(2, len(nums)):
            if i-3 >= 0: 
                nums[i] += max(nums[i-3], nums[i-2])
            else:
                nums[i] += nums[i-2]
        
        return max(nums[-1], nums[-2])