#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        e = n
        f = k
        dp = {}
        def solve(e, f):
            if e == 1: return f
            if f in (0, 1): return f
            if (e,f) in dp: return dp[(e,f)]
            ans = 2*31
            for i in range(1, f):
                tmp = 1 + max(solve(e-1, i-1), solve(e, f-i))
                ans = min(ans, tmp)
            dp[(e,f)] = ans
            return ans
        
        return solve(e,f)







#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends