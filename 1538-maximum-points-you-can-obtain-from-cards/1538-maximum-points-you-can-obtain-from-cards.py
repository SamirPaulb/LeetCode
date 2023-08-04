class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # Find minimum sub array sum of length n-k
        prefixSum = []
        s = 0
        for i in cardPoints:
            prefixSum.append(s)
            s += i
        prefixSum.append(s)
        minSubArraySum = 2**31
        for i in range(n-k, n+1):
            minSubArraySum = min(minSubArraySum, prefixSum[i] - prefixSum[i-(n-k)])
        return sum(cardPoints) - minSubArraySum