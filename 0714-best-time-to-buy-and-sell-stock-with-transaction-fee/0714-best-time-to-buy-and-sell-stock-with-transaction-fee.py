class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        obsp, ossp = -prices[0], 0
        nbsp, nssp = 0, 0
        
        for p in prices:
            nbsp = max(obsp, ossp - p)
            nssp = max(ossp, obsp + p - fee)
            
            obsp = nbsp
            ossp = nssp
        
        return ossp