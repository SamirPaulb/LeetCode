
class Solution:
    def minDist(self, arr, n, x, y):
        recent_x = -1
        recent_y = -1
        res = 2**31
        for i in range(n):
            if arr[i] == x:
                recent_x = i
                if recent_y != -1:
                    res = min(res, abs(recent_x - recent_y))
            if arr[i] == y:
                recent_y = i
                if recent_x != -1:
                    res = min(res, abs(recent_x - recent_y))
        
        return res if res != 2**31 else -1
        
        

                
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends