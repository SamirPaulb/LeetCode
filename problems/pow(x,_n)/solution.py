# https://www.youtube.com/watch?v=l0YC3876qxg
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        
        p = abs(n)
        ans = 1
        while p > 1:
            if p % 2 == 0:
                x = x*x
                p = p//2
            else:
                ans *= x
                x = x*x
                p = (p-1)//2
        
        ans *= x
        
        if n > 0: return ans
        else: return 1 / ans
        
'''
Time Complxity = O(log(n))
Space Complexity = O(1)
'''        
        

        
'''
2.00000
10
2.00000
-2
1.00000
2147483647
0.00001
2147483647
'''