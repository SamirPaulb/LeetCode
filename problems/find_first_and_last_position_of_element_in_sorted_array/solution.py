class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        # Implementing Binary Search 3 times
        # First binary search for locating any index of target.
        # Second binary search for finding Left Boundary index if target.
        # Third binary search for finding Right Boundary index of target.
        found = False
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2 
            if nums[mid] < target: l = mid + 1
            elif nums[mid] > target: r = mid - 1
            else: 
                found = True
                break
        
        if not found: return ans
        
        # Finding Left Boundary index of Target.
        l, r = 0, mid
        while l <= r:
            m = (l + r) // 2  
            if nums[m] < target: l = m + 1
            elif nums[m] > target: r = m 
            else: 
                if m == 0:
                    ans[0] = m
                    break
                if m - 1 >= 0 and nums[m - 1] != target:
                    ans[0] = m
                    break
                r = m - 1
                
        # Finding Right Boundary index of Target.
        l, r = mid, len(nums) - 1
        while l <= r:
            m = (l + r) // 2 
            if nums[m] < target: l = m + 1
            elif nums[m] > target: r = m 
            else: 
                if m == len(nums) - 1:
                    ans[1] = m
                    break
                if m + 1 < len(nums) and nums[m + 1] != target:
                    ans[1] = m
                    break
                l = m + 1
        
        return ans
                
            
            
            