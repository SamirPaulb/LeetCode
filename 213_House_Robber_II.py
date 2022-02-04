class Solution(object):
    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if nums is None or len(nums) == 0:
    #         return 0
    #     ls = len(nums)
    #     dp = [0] * ls
    #     # dp from 0 ~ ls - 2
    #     dp[0] = nums[0]
    #     for i in range(1, ls - 1):
    #         if i < 2:
    #             dp[i] = max(nums[i], dp[i - 1])
    #         else:
    #             dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    #     res = dp[ls - 2]
    #     # dp from 1 ~ ls - 1
    #     dp[0] = 0
    #     for i in range(1, ls):
    #         if i < 2:
    #             dp[i] = max(nums[i], dp[i - 1])
    #         else:
    #             dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    #     return max(res, dp[ls - 1])

    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_helper(nums, 0, len(nums) - 2),
                   self.rob_helper(nums, 1, len(nums) - 1))


    def rob_helper(self, nums, low, high):
        prevMax = currMax = 0
        for index in range(low, high + 1):
            temp = currMax
            currMax = max(prevMax + nums[index], currMax)
            prevMax = temp
        return currMax
