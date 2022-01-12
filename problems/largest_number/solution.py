class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        # bubble sort
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]
        
        ans = "".join(nums)
        
        return ans if int(ans) != 0 else "0"