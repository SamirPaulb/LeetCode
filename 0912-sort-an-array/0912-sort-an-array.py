class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
    
    def mergesort(self, arr):
        if not arr or len(arr) == 1: return arr
        n = len(arr)
        a = self.mergesort(arr[:n//2])
        b = self.mergesort(arr[n//2:])
        return self.merge(a, b)
            
    def merge(self, a, b):
        if not a or not b: return b or a
        arr = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                arr.append(a[i])
                i += 1
            else:
                arr.append(b[j])
                j += 1
        
        while i < len(a):
            arr.append(a[i])
            i += 1
        while j < len(b):
            arr.append(b[j])
            j += 1
        
        return arr