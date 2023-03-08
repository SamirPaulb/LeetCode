class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > LIS[-1]:
                LIS.append(nums[i])
            else:
                idx = bisect.bisect_left(LIS, nums[i])
                LIS[idx] = nums[i]
        
        return len(LIS)