class Solution:
    def candy(self, ratings: List[int]) -> int:
        dp = [1] * len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                dp[i] = max(1+dp[i-1], dp[i])
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                dp[i] = max(1+dp[i+1], dp[i])
        
        return sum(dp)