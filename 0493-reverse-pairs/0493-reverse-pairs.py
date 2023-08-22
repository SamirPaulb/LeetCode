class Solution:
    def __init__(self):
        self.count = 0

    def mergeSort(self, arr):

        if len(arr) > 1:
            mid = len(arr)//2
            left = self.mergeSort(arr[:mid])
            right = self.mergeSort(arr[mid:])
            
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2*right[j]:
                    j += 1
                self.count += j
            
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return arr

    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        return self.count