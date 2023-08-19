#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		res = []
		def dfs(i, s):
		    if i >= len(arr):
		        res.append(s)
		        return 
		    dfs(i+1, s)
		    dfs(i+1, s+arr[i])
        
        dfs(0, 0)
        return res
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends