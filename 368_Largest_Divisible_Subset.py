class Solution(object):
    # def largestDivisibleSubset(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     # https://discuss.leetcode.com/topic/49455/4-lines-in-python
    #     S = {-1: set()}
    #     for x in sorted(nums):
    #         # S[x] is the largest subset with x as the largest element
    #         S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
    #     return list(max(S.values(), key=len))

    def largestDivisibleSubset(self, nums):
        ls = len(nums)
        S = {-1: set()}
        for num in sorted(nums):
            candicate = []
            for key in S:
                if num % key == 0:
                    candicate.append(S[key])
            # max previous with curr
            S[num] = max(candicate, key=len) | {num}
        return 