class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sumDic = {0 : 1}
        curSum = 0
        remainder = 0
        ans = 0
        for i, ch in enumerate(nums):
            curSum += ch
            remainder = curSum % k
            if remainder < 0:
                remainder += k
            if remainder in sumDic:
                ans += sumDic[remainder] 
                sumDic[remainder] += 1
            else:
                sumDic[remainder] = 1
        
        return ans
    