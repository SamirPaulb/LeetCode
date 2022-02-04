class Solution(object):
    # def subsetsWithDup(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     nums.sort()
    #     res = []
    #     for i in range(1 << len(nums)):
    #         res.append(self.get_subsets(nums, i))
    #     # remove duplicate
    #     final_res = {}
    #     for subset in res:
    #         hash_key = ''.join([str(t) for t in subset])
    #         try:
    #             final_res[hash_key]
    #         except:
    #             final_res[hash_key] = subset
    #     return final_res.values()
    #
    # def get_subsets(self, nums, magic):
    #     res = []
    #     for i in range(len(nums)):
    #         if (1 << i) & magic != 0:
    #             res.append(nums[i])
    #     return res

    def subsetsWithDup(self, nums):
        nums.sort()
        res = [[]]
        begin = 0
        for index in range(len(nums)):
            if index == 0 or nums[index] != nums[index - 1]:
                # generate all
                begin = 0
            size = len(res)
            # use existing subsets to generate new subsets
            for j in range(begin, size):
                curr = list(res[j])
                curr.append(nums[index])
                res.append(curr)
            # avoid duplicate subsets
            begin = size
        return res
