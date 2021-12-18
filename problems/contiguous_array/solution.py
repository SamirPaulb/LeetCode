class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashMap = {0:-1}
        ans = 0
        currSum = 0
        # consider 0 as -1; 1 as +1 => is currSum ==0 => equal number of 0 and 1
        for i in range(len(nums)):
            if nums[i] == 1: currSum += 1
            else: currSum -= 1
                
            if currSum not in hashMap:
                hashMap[currSum] = i 
            else:
                ans = max(ans, i - hashMap[currSum])
        
        return ans

# nums = [0,1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1]

