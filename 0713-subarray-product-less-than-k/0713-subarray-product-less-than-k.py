class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        mul = 1
        l = 0
        res = 0
        for r in range(len(nums)):
            mul *= nums[r]
            while l <= r and mul >= k:
                mul //= nums[l]
                l += 1
            res += r-l+1
        return res