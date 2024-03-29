class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums) + target) % 2 != 0: return 0
        if abs(target) > sum(nums): return 0
        tar = (sum(nums) + target) // 2
        dp = [[0]*(tar+1) for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] =  1
        for i in range(1, len(nums)+1):
            for j in range(tar+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
        
    