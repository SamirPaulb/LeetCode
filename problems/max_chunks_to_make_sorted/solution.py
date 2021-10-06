class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_value = arr[0]
        ans = 0
        # arr = [3, 0, 1, 2, 5, 4, 8, 6, 7]
        for i, ch in enumerate(arr):
            max_value = max(max_value, ch)
            if i == max_value:
                ans += 1
        
        return ans if ans != 0 else 1
            