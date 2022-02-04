class Solution(object):
    def majorityElement(self, nums):
        # O(1) space
        ls = len(nums)
        res = []
        check_value = []
        for i in range(ls):
            if nums[i] in check_value:
                continue
            count = 1
            for j in range(i + 1, ls):
                if nums[i] == nums[j]:
                    count += 1
            if count > ls / 3:
                res.append(nums[i])
            check_value.append(nums[i])
        return res

    # def majorityElement(self, nums):
    #     # using dict
    #     count_hash = {}
    #     res = []
    #     for i in nums:
    #         try:
    #             count_hash[i] += 1
    #         except KeyError:
    #             count_hash[i] = 1
    #     for k, v in count_hash.iteritems():
    #         if v > len(nums) / 3:
    #             res.append(k)
    #     return res

    # def majorityElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     #https://leetcode.com/discuss/76542/easy-python-solution
    #     tmp = {}
    #     res = []
    #     for n in list(set(nums)):
    #         tmp[n] = nums.count(n)
    #     for k, v in tmp.iteritems():
    #         if v > len(nums) / 3:
    #             res.append(k)
    #     return res