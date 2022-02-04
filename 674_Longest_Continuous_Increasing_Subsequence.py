class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        ans = curr = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 1
        return ans
