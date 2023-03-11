class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        obsp, ocsp, ossp = -prices[0], 0, 0
        nbsp, ncsp, nssp = 0, 0, 0
        
        for p in prices:
            nbsp = max(obsp, ocsp - p)
            nssp = max(ossp, obsp + p)
            ncsp = max(ocsp, ossp)
            
            obsp, ocsp, ossp = nbsp, ncsp, nssp
        
        return ossp