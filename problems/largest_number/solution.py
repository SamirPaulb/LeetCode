class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Bubble Sort
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if str(nums[j+1]) + str(nums[j]) > str(nums[j]) + str(nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        return str(int("".join(map(str, nums))))