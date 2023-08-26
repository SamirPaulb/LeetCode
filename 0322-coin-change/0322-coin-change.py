class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def solve(i, amount):
            if amount == 0: return 0
            if amount < 0: return 2**31
            if i >= len(coins): return 2**31
            if (i, amount) in memo: return memo[(i, amount)]
            ans = min(1 + min(solve(i, amount - coins[i]), solve(i+1, amount - coins[i])), solve(i+1, amount))
            memo[(i, amount)] = ans
            return ans
        
        res = solve(0, amount)
        return res if res < 2**31 else -1