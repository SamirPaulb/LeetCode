class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        prefixSum = []
        s = 0
        for i in nums:
            prefixSum.append(s)
            s += i
        res = 1
        l = 0
        for r in range(len(nums)):
            if nums[r]*(r-l) - (prefixSum[r] - prefixSum[l]) <= k:
                res = max(res, r-l+1)
            else:
                l += 1
        print(prefixSum)
        return res