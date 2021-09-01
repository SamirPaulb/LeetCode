class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_rob(nums):
            dp = [0]*len(nums)
            for i in range(len(nums)):
                if i == 0:
                    dp[i] = nums[i]
                elif i == 1:
                    dp[i] = max(nums[i], nums[i-1])
                else:
                    dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            return max(dp[-1], dp[-2])
        if len(nums) <= 2:
            return max([0]+nums)
        return house_rob(nums)