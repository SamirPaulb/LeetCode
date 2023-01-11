class Solution:
    def equalSubstring(self, s, t, maxCost):
        costs = []
        for i in range(len(s)):
            costs.append(abs(ord(s[i]) - ord(t[i])))
        
        curCost = res = l = 0
        for r in range(len(s)):
            curCost += costs[r]
            if curCost <= maxCost:
                res = max(res, r-l+1)
            else:
                curCost -= costs[l]
                l += 1
        
        return res