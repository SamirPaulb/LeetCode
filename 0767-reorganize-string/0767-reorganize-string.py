class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = collections.Counter(s)
        minHeap = []
        for c in cnt:
            heapq.heappush(minHeap, (-cnt[c], c))
        res = ""
        while len(minHeap) >= 2:
            ac, a = heapq.heappop(minHeap)
            bc, b = heapq.heappop(minHeap)
            res += a
            res += b
            if ac < -1: heapq.heappush(minHeap, (ac+1, a))
            if bc < -1: heapq.heappush(minHeap, (bc+1, b))
            
        if len(minHeap) == 1:
            if res and res[-1] == minHeap[0][-1] or minHeap[0][0] < -1: return ""
            res += heapq.heappop(minHeap)[1]
        return res
