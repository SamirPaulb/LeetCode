class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        if len(nums) == len(index):
            newL = []
            for i in range(len(nums)):
                if index[i] < len(nums):
                    val = nums[i]
                    target = index[i]
                    if newL == []:
                        newL.append(val)
                    else:
                        newL.insert(target, val)
        
        return newL
                