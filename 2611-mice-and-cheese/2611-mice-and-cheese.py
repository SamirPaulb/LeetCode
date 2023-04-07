class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        minHeap = []
        for i in range(len(reward1)):
            r = reward2[i] - reward1[i]
            heapq.heappush(minHeap, (r,i))
        
        res = 0
        visited = set()
        while k:
            r, i = heapq.heappop(minHeap)
            res += reward1[i]
            visited.add(i)
            k -= 1
        
        for i in range(len(reward2)):
            if i not in visited:
                res += reward2[i]
        
        return res