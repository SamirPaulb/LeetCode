class Solution:
    def longestSubarray(self, nums):
        l = z = res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                z += 1
            while z > 1:
                if nums[l] == 0: 
                    z -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res-1