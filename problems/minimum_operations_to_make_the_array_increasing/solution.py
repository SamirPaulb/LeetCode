class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                a = nums[i+1]
                nums[i+1] +=  nums[i] - nums[i+1] + 1
                s = s + (nums[i+1] -a)
            
        return s
            
        