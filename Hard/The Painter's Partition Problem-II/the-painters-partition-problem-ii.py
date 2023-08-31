#User function Template for python3

class Solution:
    def minTime (self, arr, n, k):
        #code here
        def check(mid):
            s = 0
            cnt = 1
            for a in arr:
                s += a
                if s > mid:
                    cnt += 1
                    s = a
            return cnt <= k
        
        l, r = max(arr), sum(arr)
        res = 2**31
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1
        
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr,n,k))
# } Driver Code Ends