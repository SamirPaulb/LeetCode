class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Making elements string
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        # Applying Bubble sort
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        res = "".join(nums)
        return res if int(res) != 0 else "0" 