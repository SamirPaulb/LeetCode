class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0; r = k-1; res = 2**31
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        
        return res