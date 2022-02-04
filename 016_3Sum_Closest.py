# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
class Solution(object):
    def threeSumClosest(self, nums, target):
        ls = len(nums)
        sort_nums = sorted(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(ls - 2):
            j, k = i + 1, ls - 1
            while j < k:
                temp = sort_nums[i] + sort_nums[j] + sort_nums[k]
                if abs(target - temp) < abs(target - res):
                    res = temp
                if temp < target:
                    j += 1
                else:
                    k -= 1
        return res


