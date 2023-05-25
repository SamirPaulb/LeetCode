#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		dist = [2**31] * n
		for i in range(n):
		    for j in range(len(edges)):
		        fr, to, wt = edges[j]
		        if dist[fr] + wt < dist[to]:
		            dist[to] = dist[fr] + wt
        
        for j in range(len(edges)):
	        fr, to, wt = edges[j]
	        if dist[fr] + wt < dist[to]:
	            return 1
	
		return 0
		            
		            
		            
		            
		            
		            
		            
		            
		            
		            
		            
		            
		            #{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

# } Driver Code Ends