import heapq
class KthLargest:
    """
    The idea is to ALWAYS maintain a MIN heap with only K elements
    - in this case, the K-the largest element (in the stream)
    - will always be at the root position
    """
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for num in nums:
            self.add(num) # add elements using the function below
        
    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        
        # if after adding the new item causes 
        # the heap size to increase beyond k, 
        # then pop out the smallest element 
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)
            
        return self.heap[0] # the root element