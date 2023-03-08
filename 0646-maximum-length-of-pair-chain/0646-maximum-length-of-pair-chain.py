class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1]*len(pairs)
        for i in range(len(pairs)):
            tmp = 1
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    tmp = max(tmp, dp[j]+1)
            dp[i] = tmp
        
        return max(dp)