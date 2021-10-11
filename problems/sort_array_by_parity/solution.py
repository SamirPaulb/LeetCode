class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        arr = []
        while i < len(nums):
            if nums[i] % 2 != 0:
                arr.append(nums[i])
                nums.pop(i)
            else: i += 1
        
        nums += arr
        
        return nums