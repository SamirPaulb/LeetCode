class Solution:
    def countVowelPermutation(self, n: int) -> int:
        rules = {'a':'e', 'e':'ai', 'i':'aeou', 'o':'iu', 'u':'a'}
        dp = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
        for i in range(1, n):
            new_dp = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
            for key, values in rules.items():
                for v in values:
                    new_dp[key] += dp[v]
            dp = new_dp
        return sum(dp.values()) % 1000000007
                    
            