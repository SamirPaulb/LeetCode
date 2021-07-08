class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
                n -= 1
            else:
                i += 1
        