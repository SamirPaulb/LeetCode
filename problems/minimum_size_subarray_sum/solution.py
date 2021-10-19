# https://www.youtube.com/watch?v=b7wMv62Y1l4&t=241s
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        
        start = end = 0
        s = 0
        ans = len(nums)
        
        while end < len(nums):
            while s < target and end < len(nums):
                s += nums[end]
                end += 1
                        
            while s >= target and start < end:
                ans = min(ans, end - start)
                s -= nums[start]
                start += 1
            
        return ans