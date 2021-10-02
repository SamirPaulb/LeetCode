class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        minsofar = nums[0]
        
        for i in range(1, len(nums)):
            ans = max(ans, nums[i] - minsofar)
            minsofar = min(minsofar, nums[i])
            
        return ans if ans != 0 else -1