class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l = r = res = 0
        recentMin = recentMax = -1
        while r < len(nums):
            while r < len(nums) and minK <= nums[r] <= maxK:
                if nums[r] == minK:
                    recentMin = r
                if nums[r] == maxK:
                    recentMax = r
                if recentMin != -1 and recentMax != -1:
                    res += min(recentMin, recentMax) - l + 1
                r += 1
            recentMin = recentMax = -1
            l = r+1
            r += 1
        
        return res