# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# https://youtu.be/h_6MldQ8vB8?t=121

class Solution:
    def canPartitionKSubsets(self, nums, k):
        nums.sort(reverse=True) # Game Changer 1
        buck, kSum = [0] * k, sum(nums) // k
        def dfs(idx):
            if idx == len(nums): return len(set(buck)) == 1
            for i in range(k):
                buck[i] += nums[idx]
                if buck[i] <= kSum and dfs(idx + 1): return True
                buck[i] -= nums[idx]
                if buck[i] == 0: break # Game Changer 2
            return False
        return dfs(0)

    
    
# Time: O(k * 2^n)
# Space: O(k * 2^n)