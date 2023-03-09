class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums))
        count = [1]*(len(nums))
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = 1 + dp[j]
                    count[i] = count[j]
                elif nums[j] < nums[i] and dp[j] + 1 == dp[i]:
                    count[i] += count[j]
        maxi = max(dp)
        res = 0
        for i in range(len(nums)):
            if dp[i] == maxi:
                res += count[i]
            
        return res