class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        for i in range(len(nums)):
            if sum(nums[i:i+3]) > 2* max(nums[i:i+3]):
                return sum(nums[i:i+3])
        return 0
    
    