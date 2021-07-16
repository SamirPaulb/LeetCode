class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        n = len(nums) - 1
        while i < n:
            if nums[i] == 0:
                a = nums[i]
                nums.remove(a)
                nums.append(a)
                n -= 1
            else:
                i += 1
        return nums
        