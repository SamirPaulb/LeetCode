# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums, k):
        nums.sort(reverse=True) # Game Changer 1
        subsets, target = [0] * k, sum(nums)//k
        
        def backtrack(idx):
            if idx == len(nums):
                return True
            for i in range(k):
                subsets[i] += nums[idx]
                if subsets[i] <= target and backtrack(idx+1): 
                    return True
                subsets[i] -= nums[idx]
                if subsets[i] == 0: 
                    break
            return False
        
        return backtrack(0)
        

    
    
# Time: O(k * 2^n)
# Space: O(k * 2^n)