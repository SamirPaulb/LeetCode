class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums: return
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
        res = "".join(nums)
        if int(res) == 0: return "0"
        return res
    