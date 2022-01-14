class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        minDiff = float("inf")
        for i in range(len(arr)-1):
            minDiff = min(minDiff, arr[i+1] - arr[i])
        
        res = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == minDiff:
                res.append([arr[i], arr[i+1]])
        
        return res