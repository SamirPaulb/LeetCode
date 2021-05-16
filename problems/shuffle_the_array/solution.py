class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newL = []
        if len(nums) == 2*n:
            for i in range(n):
                newL.append(nums[i])
                newL.append(nums[n+i])
        return newL