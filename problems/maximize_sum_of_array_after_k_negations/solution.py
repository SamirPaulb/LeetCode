class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for  i in range(k):
            m = min(nums)
            mi = nums.index(m)
            nums[mi] = -m
        return sum(nums)