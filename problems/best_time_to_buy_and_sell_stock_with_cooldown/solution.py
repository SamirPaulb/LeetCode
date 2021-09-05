# https://www.youtube.com/watch?v=GY0O57llkKQ
# First Solve -->> 714. Best Time to Buy and Sell Stock with Transaction Fee -->> then solve this problem

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        obsp = -prices[0] # obsp = Old Brought state Profit
        ossp = 0 # ossp = Old Sold State Profit
        ocsp = 0 # ocsp = Old Cold State Profit
        for i in range(1, len(prices)):
            nbsp = 0 # nbsp = New Brought State Profit
            nssp = 0 # nssp = New Sold State Profit
            ncsp = 0 # ncsp = New Cold State Profit
            
            nbsp = max(ocsp - prices[i], obsp)
            nssp = max(obsp + prices[i], ossp)
            ncsp = max(ossp, ocsp)
            
            obsp = nbsp
            ossp = nssp
            ocsp = ncsp
        
        return ossp