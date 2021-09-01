class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for i in arr2:
            a = arr1.count(i)
            for j in range(a):
                ans.append(i)
                arr1.remove(i)
        if len(arr1):
            arr1.sort()
            ans += arr1
        return ans