#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
		# code here
		dp = Arr.copy()
		for r in range(1, len(Arr)):
		    for l in range(r):
		        if Arr[l] < Arr[r]:
		            dp[r] = max(dp[r], Arr[r] + dp[l])
		return max(dp)
		
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends