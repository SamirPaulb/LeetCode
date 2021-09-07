class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) == 1: return 0
        res = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            this_max = max(nums[-1]-k, nums[i]+k)
            this_min = min(nums[0]+k, nums[i+1]-k)
            res = min(res, this_max - this_min)
        return res