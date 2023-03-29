class Solution:
    def maxSatisfaction(self, A: List[int]) -> int:
        A.sort()
        res = total = 0
        while A and A[-1] + total >= 0:
            total += A.pop()
            res += total
        return res