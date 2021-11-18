class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        start, end = 0, len(nums) - 1
        a = None
        while start <= end:
            mid = (start + end) // 2 
            if nums[mid] == target: 
                a = mid
                break
            if target < nums[mid]: end = mid - 1
            if target > nums[mid]: start = mid + 1
        
        if a == None: return ans
        # To find the left limit fo target
        i = a
        while i >= 0 and nums[i] == target:
            i -= 1
        ans[0] = i + 1
        # To find the right limit of target
        i = a
        while i < len(nums) and nums[i] == target:
            i += 1
        ans[1] = i - 1
        
        return ans