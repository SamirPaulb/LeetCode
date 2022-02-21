class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumIndexDic = {0:-1}
        
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            curSum %= k
            
            if curSum in sumIndexDic:
                if i - sumIndexDic[curSum] >= 2: return True
            else:
                sumIndexDic[curSum] = i
        
        return False