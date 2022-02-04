class Solution(object):
    # def summaryRanges(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[str]
    #     """
    #     if nums is None or len(nums) == 0:
    #         return []
    #     res = []
    #     start, prev, ls = nums[0], nums[0], len(nums)
    #     for i in range(ls):
    #         curr = nums[i]
    #         if curr - prev > 1:
    #             if start == prev:
    #                 res.append("%d" % start)
    #             else:
    #                 res.append("%d->%d" % (start, prev))
    #             start = curr
    #         prev = curr
    #     if start == prev:
    #         res.append("%d" % start)
    #     else:
    #         res.append("%d->%d" % (start, prev))
    #     return res

    def summaryRanges(self, nums):
        res = []
        start, ls = 0, len(nums)
        for i in range(ls):
            if i + 1 <  ls and nums[i + 1] == nums[i] + 1:
                continue
            if i == start:
                res.append(str(nums[start]))
            else:
                res.append("%d->%d" % (nums[start], nums[i]))
            start = i + 1
        return res
