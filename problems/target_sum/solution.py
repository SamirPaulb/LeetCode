class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums): return 0
        if (target + sum(nums)) % 2 != 0: return 0
        s1 = (target + sum(nums)) // 2
        dp = [[0]*(s1 + 1) for i in range(len(nums)+1)]
        for i in range(len(nums) + 1):
            dp[i][0] = 1
        
        for i in range(1, len(nums)+1):
            for j in range(s1 + 1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        #print(dp)
        return dp[-1][-1]