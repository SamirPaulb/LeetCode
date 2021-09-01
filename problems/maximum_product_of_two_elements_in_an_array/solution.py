class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = (nums[-1]-1)*(nums[-2]-1)
        b = (nums[0]-1)*(nums[1]-1)
        return max(a, b)