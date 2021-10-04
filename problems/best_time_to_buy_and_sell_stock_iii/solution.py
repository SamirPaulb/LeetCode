class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Devide the array prices in two parts and apply buy and sell stock 1 approach on both part
        # But that would take O(n*n)
        # Trick:
        # make two new array. One to store the first part and other the second part
        # Add both elements of the 2 array of same indexed
        # Make Firt array by forward traversal of Prices
        # Make Second array by Reversed traversal of Prices
        n = len(prices)
        profit1 = [0] * n
        profit2 = [0] * n
        
        minSoFar = prices[0]
        maxProfitSoFar = 0
        for i in range(n):
            maxProfitSoFar = max(maxProfitSoFar, prices[i] - minSoFar)
            minSoFar = min(minSoFar, prices[i])
            profit1[i] = maxProfitSoFar
        
        maxSoFar = prices[-1]
        maxProfitSoFar = 0
        for i in range(n-1, -1, -1):
            maxProfitSoFar = max(maxProfitSoFar, maxSoFar - prices[i])
            maxSoFar = max(maxSoFar, prices[i])
            profit2[i] = maxProfitSoFar
        
        ans = 0
        for i in range(n):
            ans = max(ans, profit1[i] + profit2[i])
        
        return ans
    
    # Time Complexity = O(n)
    # Space Complexity = O(n)