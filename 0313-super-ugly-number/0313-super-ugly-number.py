# https://leetcode.com/problems/super-ugly-number/

'''
Same as: 264. Ugly Number II
'''

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        primes.sort()
        pointers = [0] * len(primes)
        dp = [1] * n
        
        for i in range(1, n):
            multiples = [0]*len(primes)
            for j in range(len(primes)):
                multiples[j] = dp[pointers[j]] * primes[j]
            dp[i] = min(multiples)
            
            for j in range(len(primes)):
                if dp[i] % multiples[j] == 0: pointers[j] += 1
            # print(dp[i], multiples, pointers)
        # print(dp)
        return dp[-1]