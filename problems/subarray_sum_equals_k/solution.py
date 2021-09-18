class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        hashMap = {}
        curSum = 0
        
        if len(nums) == 0:
            return 0
        
        hashMap[0] = 1
        
        for i in range(len(nums)):
            curSum += nums[i]
                
            if (curSum - k) in hashMap:
                count += hashMap[curSum - k]
                
            if curSum in hashMap:
                hashMap[curSum] += 1
            else:
                hashMap[curSum] = 1
        
        return count
                