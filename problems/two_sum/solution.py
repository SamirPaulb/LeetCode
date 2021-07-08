class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            leftover =  target - nums[i]
            if (leftover in nums ) and (nums.index(leftover) != i):
                return [i, nums.index(leftover)]