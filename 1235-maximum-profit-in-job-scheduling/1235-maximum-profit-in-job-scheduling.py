class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key = lambda x:x[1])
        
        dpEndTime = [0]
        dpProfit = [0]
        
        for start, end, profit in jobs:
            idx = self.rightMostNonOverlapping(dpEndTime, start) - 1
            lastProfit = dpProfit[-1]
            curProfit = dpProfit[idx] + profit
            if lastProfit < curProfit:
                dpEndTime.append(end)
                dpProfit.append(curProfit)
        
        return dpProfit[-1]
    
    
    def rightMostNonOverlapping(self, dpEndTime, start):
        l = 0
        r = len(dpEndTime) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if dpEndTime[mid] <= start:
                l = mid + 1
            else:
                r = mid - 1
        
        return l