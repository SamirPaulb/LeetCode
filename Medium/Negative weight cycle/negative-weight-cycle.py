#User function Template for python3
import heapq

class Solution:
    def isNegativeWeightCycle(self, n, edges):
        #Code here
        adjList = {i:[] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append((edge[2], edge[1])) # (weight. node)
            
        for i in range(n):
            visited = [False] * n
            minHeap = [(0, i)]
            while minHeap:
                dist, node = heapq.heappop(minHeap)
                if visited[node] == True: 
                    if node == i and dist < 0: return 1
                    continue
                visited[node] = True
                for c in adjList[node]:
                    heapq.heappush(minHeap, (dist + c[0], c[1]))
        
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