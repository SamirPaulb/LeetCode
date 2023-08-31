class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if m == 0 or m == len(nums)-1:
                return nums[m]
            if nums[m-1] != nums[m] != nums[m+1]: 
                return nums[m]
            if m%2 == 0:
                if nums[m] == nums[m+1]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] == nums[m+1]:
                    r = m - 1
                else:
                    l = m + 1
        
        return nums[l]