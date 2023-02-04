class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i, ch in enumerate(nums):
            nums[i] = int(ch)
        nums.sort()
        return str(nums[-k])