class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        arr = [0]*len(values)
        maxi = -2**31
        for j in range(len(values)-1, -1, -1):
            arr[j] = maxi
            maxi = max(maxi, values[j] - j)
        
        res = 0
        for i in range(len(values)-1):
            res = max(res, values[i] + i + arr[i])
            
        return res