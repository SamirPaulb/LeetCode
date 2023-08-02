class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = mid = 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                mid -= 1
                high -= 1
            mid += 1
        
        return nums
