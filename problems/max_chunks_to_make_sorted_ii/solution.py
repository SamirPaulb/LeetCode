# https://www.youtube.com/watch?v=GxTo3agdnjs
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        leftMax = [0] * len(arr)
        rightMin = [0] * len(arr)
        
        l, r = 0, len(arr)-1
        lM, rM = arr[0], arr[-1]
        while l < len(arr) and r >= 0:
            lM = max(lM, arr[l])
            rM = min(rM, arr[r])
            leftMax[l] = lM
            rightMin[r] = rM
            l += 1
            r -= 1
        
        ans = 1
        for i in range(len(arr) - 1):
            if leftMax[i] <= rightMin[i + 1]: ans += 1
                
        return ans