class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        prefixSum = []
        s = 0
        for i in nums:
            prefixSum.append(s)
            s += i
        
        res = 1
        for r in range(len(nums)):
            if nums[r] * (r-l) - (prefixSum[r] - prefixSum[l]) <= k:
                res = max(res, r-l+1)
                # print(r,l)
            else:
                l += 1
        return res