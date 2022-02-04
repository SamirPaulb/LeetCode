class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        max_here = min_here = max_so_far = nums[0]
        for i in range(1, len(nums)):
            mx, mn = max_here, min_here
            max_here = max(max(mx * nums[i], nums[i]), mn * nums[i])
            min_here = min(min(mx * nums[i], nums[i]), mn * nums[i])
            max_so_far = max(max_here, max_so_far)
        return max_so_far