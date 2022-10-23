class Solution:  
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        low, high = min(nums), max(nums)
        while (low <= high):
            target = (low+high)//2
            cost_curr = self.cal_cost(nums, cost, target)
            cost_right = self.cal_cost(nums, cost, target+1)
            if cost_right < cost_curr:
                low = target+1
            else:   # cost_right < cost:
                high = target-1
        return self.cal_cost(nums, cost, low)
    
    def cal_cost(self, nums, cost, target):
        ans = 0
        for n, c in zip(nums, cost):
            ans += abs(n-target) * c
        return ans