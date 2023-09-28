#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		dist = [2**31] * n
		dist[0] = 0
		for i in range(n):
		    for j in range(len(edges)):
		        f, t, w = edges[j]
		        if dist[f] != 2*31 and dist[f] + w < dist[t]:
		            dist[t] = dist[f] + w
		
		for j in range(len(edges)):
		    f, t, w = edges[j]
	        if dist[f] != 2*31 and dist[f] + w < dist[t]:
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