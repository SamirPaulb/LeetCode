class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_so_far = values[0] # max_so_far = values[i] + i
        ans = 0  # ans = max_so_far + values[j] - j
        for j in range(1, len(values)):
            ans = max(ans, max_so_far + values[j] - j)
            max_so_far = max(max_so_far, values[j] + j)
        return ans