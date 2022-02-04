class Solution(object):
    # def canPartition(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     if nums is None or len(nums) == 0:
    #         return True
    #     volumn = 0
    #     for num in nums:
    #         volumn += num
    #     # if sum is odd then false
    #     if volumn % 2 != 0:
    #         return False
    #     # if sum of some elements can be half of total sum then true
    #     volumn /= 2
    #     dp = [False] * (volumn + 1)
    #     dp[0] = True
    #     for i in range(1, len(nums) + 1):
    #         for j in range(volumn, nums[i - 1] - 1, -1):
    #             dp[j] = dp[j] or dp[j - nums[i - 1]]
    #     return dp[volumn]

    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum & 1:
            return False
        # if sum of some elements can be half of total sum then true
        target = total_sum >> 1
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] | dp[i - num]
        return dp[target] == 1