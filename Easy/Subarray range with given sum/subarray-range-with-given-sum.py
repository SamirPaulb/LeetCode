#User function Template for python3
import collections

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, n, sum):
        #Your code here
        s = res = 0
        cnt = collections.Counter()
        cnt[0] = 1
        for i in arr:
            s += i
            k = s-sum
            res += cnt[k]
            cnt[s] += 1
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        sum=int(input())
        
        print(Solution().subArraySum(arr, n, sum))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends