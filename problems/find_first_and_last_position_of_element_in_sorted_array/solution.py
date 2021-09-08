class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1,-1]
        arr = []
        def binary_search(nums, high, low, target):
            if high >= low:
                mid = (high + low) // 2
                if target == nums[mid]:
                    arr.append(mid)
                if nums[mid] > target or ((mid-1)>=0 and nums[mid-1] == target):
                    binary_search(nums, mid-1, low, target)
                if nums[mid] < target or ((mid+1)<len(nums) and nums[mid+1] == target):
                    binary_search(nums, high, mid+1, target)
                
            return arr
        
        binary_search(nums, len(nums)-1, 0, target)
        if len(arr) == 0: return [-1,-1]
        
        return [min(arr), max(arr)]
    