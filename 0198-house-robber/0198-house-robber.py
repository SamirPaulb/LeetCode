class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            prev = 0
            if i-2 >= 0:
                prev = nums[i-2]
            elif i-3 >= 0:
                prev = max(prev, nums[i-3])
            nums[i] += prev
            nums[i] = max(nums[i-1], nums[i])
        
        return max(nums)