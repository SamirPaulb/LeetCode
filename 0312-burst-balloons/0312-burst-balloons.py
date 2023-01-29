'''# https://leetcode.com/problems/burst-balloons/
# https://youtu.be/VFskby7lUbw

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        
        def dfs(l, r):
            if l > r: return 0
            if (l,r) in dp: return dp[(l,r)]
            dp[(l,r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)
            return dp[(l,r)]
        
        return dfs(1, len(nums)-2)
    
    
    
# Time: O(N^3)
# Space: O(N^2)'''

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1: # in memory or gap < 2
                return dp[i][j]
            coins = 0
            for k in range(i+1, j): # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n-1)