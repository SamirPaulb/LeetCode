class Solution:  
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        low, high = min(nums), max(nums)
        while (low <= high):
            target = (low+high)//2
            cost_curr = self.cal_cost(nums, cost, target)
            cost_left = self.cal_cost(nums, cost, target-1)
            cost_right = self.cal_cost(nums, cost, target+1)
            if cost_left >= cost_curr <= cost_right:
                return cost_curr
            elif cost_left < cost_curr:
                high = target-1
            else:   # cost_right < cost:
                low = target+1
        return cal_cost(low)
    
    def cal_cost(self, nums, cost, target):
        ans = 0
        for n, c in zip(nums, cost):
            ans += abs(n-target) * c
        return ans