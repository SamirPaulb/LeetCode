class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        s1 - s2 = target     ----equation 1
        s1 + s2 = sun(nums)  ----equation 2
        solving eq1 + eq2, we get:
        =>  2 * s1 = target + sum(nums)
        =>  s1 = (target + sum(nums)) / 2
        so, we have to find a subset s1 in nums.
        # https://www.youtube.com/watch?v=MqYLmIzl8sQ
        '''
        sumOfNums = sum(nums)
        n = len(nums)
        
        if abs(target) > sumOfNums:  # nums = [10], target = -100
            return 0
        
        # 2 * s1 = (target + sum(nums))  =>  (target + sum(nums)) must be an even number
        if (target + sumOfNums) % 2 != 0:
            return 0
        
        s1 = (sumOfNums + target) // 2
        
        # DP Table
        t = [[0] * (s1 + 1) for i in range(n + 1)]
		
        t[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(s1 + 1):
                
                if nums[i - 1] <= j:
                    t[i][j] = t[i - 1][j] + t[i - 1][j - nums[i - 1]]
                
                else:
                    t[i][j] = t[i-1][j]
            
        return t[n][s1]
            