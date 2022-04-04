class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [-1] * (max(days)+1)
        days = set(days)
        dp[0] = 0
        
        for i in range(1, len(dp)):
            if i in days:
                if i >= 30:
                    dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])
                elif 7 <= i < 30:
                    dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], costs[2])
                else:
                    dp[i] = min(dp[i-1] + costs[0], costs[1], costs[2])
            else:
                dp[i] = dp[i-1]

        return dp[max(days)]