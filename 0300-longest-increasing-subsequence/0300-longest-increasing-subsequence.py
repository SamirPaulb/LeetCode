class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [nums[0]]
        
        def bis_left(target):
            l, r = 0, len(LIS)-1
            while l <= r:
                mid = l + (r-l)//2
                if LIS[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        for i in range(1, len(nums)):
            if nums[i] > LIS[-1]:
                LIS.append(nums[i])
            else:
                idx = bis_left(nums[i])
                LIS[idx] = nums[i]
        
        return len(LIS)