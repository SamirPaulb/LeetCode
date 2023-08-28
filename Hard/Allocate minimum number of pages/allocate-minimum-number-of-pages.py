class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        if len(A) < M: return -1
        
        def check(m):
            s = 0
            n = 1
            for a in A:
                s += a
                if s > m:
                    s = a
                    n += 1
            return n <= M 
        
        l, r = max(A), sum(A)
        res = 2**31
        while l <= r:
            m = l + (r-l)//2
            if check(m):
                res = min(res, m)
                r = m-1
            else:
                l = m+1
        return res if r != 2**31 else -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends