class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
    
        # Method 1 : Kadane's Algorithm
        if max(A) <= 0:
            return max(A)
        
        max_sum = curr_max = min_sum = curr_min = A[0] 
        
        for i in range(1, len(A)): 
            curr_max = max(A[i], curr_max + A[i]) 
            max_sum = max(max_sum, curr_max)
            curr_min = min(A[i], curr_min + A[i]) 
            min_sum = min(min_sum, curr_min)
            
        return max(max_sum, sum(A) - min_sum)
            
        '''
        # Method 2 : Dynamic Programming
        if max(A) <= 0:
            return max(A)
            
        max_dp = [i for i in A]
        min_dp = [i for i in A]
        
        for i in range(1,len(A)):
            if max_dp[i-1] > 0:
                max_dp[i] += max_dp[i-1]
            if min_dp[i-1] < 0:
                min_dp[i] += min_dp[i-1]

        return max(max(max_dp), sum(A) - min(min_dp))
		'''
		