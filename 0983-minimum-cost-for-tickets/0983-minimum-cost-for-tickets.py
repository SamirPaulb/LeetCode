class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(max(days)+1)
        days = set(days)
        
        for i in range(1, max(days)+1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                val = dp[i-1] + costs[0]
                val = min(val, dp[i-7] + costs[1]) if i-7 >= 0 else min(val, dp[0] + costs[1])
                val = min(val, dp[i-30] + costs[2]) if i-30 >= 0 else min(val, dp[0] + costs[2])
                dp[i] = val
        
        return dp[-1]