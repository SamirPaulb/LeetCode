# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# https://youtu.be/Tuc-rjJbsXU

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)  # length of LIS
        count = [1]*len(nums)   # count of LIS
        
        for r in range(len(nums)):
            for l in range(r):
                if nums[l] < nums[r] and dp[l] + 1 > dp[r]:
                    dp[r] = dp[l] + 1
                    count[r] = count[l]
                elif nums[l] < nums[r] and dp[l] + 1 == dp[r]:
                    count[r] += count[l]
        
        maxi = max(dp)
        res = 0
        for i in range(len(nums)):
            if dp[i] == maxi:
                res += count[i]
        # print(nums)
        # print(dp)
        # print(count)
        return res