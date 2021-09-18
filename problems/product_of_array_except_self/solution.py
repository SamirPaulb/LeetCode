class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            output[i] *= prod
        
        prod = 1
        for i in range(len(nums)-2, -1, -1):
            prod *= nums[i+1]
            output[i] *= prod
        
        return output