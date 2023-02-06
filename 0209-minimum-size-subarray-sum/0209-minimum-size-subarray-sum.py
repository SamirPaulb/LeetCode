class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        tmp, res = 0, 2**31
        while r < len(nums):
            tmp += nums[r]
            while tmp >= target:
                res = min(res, r-l+1)
                tmp -= nums[l]
                l += 1
            r += 1
        
        return res if res != 2**31 else 0
                