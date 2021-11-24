class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target: return mid
            if nums[start] <= nums[mid]: # Left side of Mid is SORTED
                if nums[start] <= target < nums[mid]:
                    end = mid
                else: start = mid + 1
            else: # Right side of Mid is SORTED
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else: end = mid
        
        return -1
    
    
    
    '''
[4,5,6,7,0,1,2]
0
[4,5,6,7,0,1,2]
3
[1]
0
[5,1,3]
3
    
    '''