class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1

        while ( start <= end ):
            mid = ( start + end ) // 2
            # found the element
            if nums[mid] == target:
                return mid
            # Couldn't find the element in the list
            elif( start == mid == end ):
                return -1
            
            # start is less than mid, list is in increasing order                
            elif ( nums[start] <= nums[mid] ):
                
                # target is greater than equal to start & smaller than mid
                if( nums[start] <= target < nums[mid] ):
                    end = mid
                
                # target is smaller than start & mid
                # target is greater than start & greater than mid
                else:
                    start = mid + 1
            
            # start is greater than mid, list is pivoted
            else: #( nums[start] > nums[mid] ):
                # target is smaller than start & greater than mid
                if ( nums[mid] < target < nums[start] ):
                    start = mid + 1
                
                # target is smaller than start & smaller than mid
                # target is greater than start & greater than mid
                else:
                    end = mid

        return -1