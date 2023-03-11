class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pb, ps = -prices[0], 0
        cb, cs = 0, 0
        
        for p in prices[1:]:
            cb = max(pb, ps - p)
            cs = max(ps, pb + p - fee)
            
            pb = cb
            ps = cs
        
        return ps