class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, ch in enumerate(nums):
            n = target - ch
            if n not in dic:
                dic[ch] = i
            else:
                return [dic[n], i]
        