class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalsum = sum(nums)
        leftsum = 0
        for i, v in enumerate(nums):
            # leftsum == rightsum
            if leftsum == totalsum - leftsum - v:
                return i
            leftsum += v
        return -1
