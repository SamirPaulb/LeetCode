class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = 0
        taken = set()
        l = 0
        res = 0
        for r in range(len(nums)):
            while nums[r] in taken:
                taken.remove(nums[l])
                s -= nums[l]
                l += 1
            s += nums[r]
            taken.add(nums[r])
            res = max(res, s)
        return res