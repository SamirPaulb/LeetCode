class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        hashMap = {0:1}
        curSum = 0
        
        for i in nums:
            curSum += i
            if (curSum - k) in hashMap:
                count += hashMap[curSum - k]
            if curSum in hashMap:
                hashMap[curSum] += 1
            else:
                hashMap[curSum] = 1
        
        return count