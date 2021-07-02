from bisect import bisect, bisect_left

class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        ind = bisect_left(arr, x)
        if ind == n or ind > 0 and arr[ind] + arr[ind-1] >= 2*x:
            ind -= 1

        beg, end = ind, ind
        for i in range(k-1):
            if beg == 0: end += 1
            elif end == n-1: beg -= 1
            else:
                if arr[end+1] + arr[beg-1] >= 2*x:
                    beg -= 1
                else:
                    end += 1

        return arr[beg:end+1]