class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        if self.right and -self.left[0] > self.right[0]:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.left) + 1 < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        if len(self.right) + 1 < len(self.left):
            heapq.heappush(self.right, -heapq.heappop(self.left))
                                                                
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        if len(self.right) > len(self.left):
            return self.right[0]
        return (-self.left[0] + self.right[0])/2
    
