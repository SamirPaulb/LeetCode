# https://www.youtube.com/watch?v=pTQB9wbIpfU

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        obsp = -prices[0]  # obsp = Old Brought State Profit
        ossp = 0  # ossp = Old Sale State Profite
        for i in range(1, len(prices)):
            nbsp = 0  # nbsp = New Brought State Profit
            nssp = 0  # nssp = New Sale State Profit
            nbsp = max(ossp - prices[i], obsp)
            nssp = max(obsp + prices[i]-fee, ossp)
            obsp = nbsp
            ossp = nssp
        return ossp