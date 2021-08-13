class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(nums, i, res):
            if i == len(nums): return res
            include = helper(nums, i+1, nums[i]^res)
            exclude = helper(nums, i+1, res)
            return include + exclude
        return helper(nums, 0, 0)
        