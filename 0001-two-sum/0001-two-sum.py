class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        taken = {}
        for i, num in enumerate(nums):
            if target - num in taken: 
                return [taken[target - num], i]
            taken[num] = i
        return False