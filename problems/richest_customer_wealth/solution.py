class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        LL = []
        for  i in range(len(accounts)):
            LL.append(sum(accounts[i]))
        return max(LL)
        