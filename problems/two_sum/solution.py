class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in dic: return [dic[n], i]
            if nums[i] not in dic: dic[nums[i]] = i
            