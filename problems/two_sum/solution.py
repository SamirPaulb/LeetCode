class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i, ch in enumerate(nums):
            n = target - ch
            if n not in myDict:
                myDict[ch] = i
            else:
                return [myDict[n], i]