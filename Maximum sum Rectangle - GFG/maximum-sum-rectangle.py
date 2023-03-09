#User function Template for python3


class Solution:
    def maximumSumRectangle(self,R,C,M):
        #code here
        def kadanes(arr):
            cs = 0; ms = arr[0]
            for a in arr:
                cs = max(a, cs + a)
                ms = max(ms, cs)
            return ms
        
        res = kadanes(M[0])
        for i in range(R):
            arr = [0]*C
            for r in range(i, -1, -1):
                for c in range(C):
                    arr[c] += M[r][c]
                res = max(res, kadanes(arr))
        
        return res
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().strip())
    for _ in range(t):
        N,M=map(int,sys.stdin.readline().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,sys.stdin.readline().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.maximumSumRectangle(N,M,a))
# } Driver Code Ends