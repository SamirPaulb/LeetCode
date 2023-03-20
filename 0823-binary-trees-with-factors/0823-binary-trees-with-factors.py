class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        count = collections.Counter()
        res = 0
        for i in range(len(arr)):
            count[arr[i]] += 1
            tmp = count[arr[i]] 
            l, r = 0, i-1
            while l <= r:
                if arr[l] * arr[r] < arr[i]:
                    l += 1 
                elif arr[l] * arr[r] > arr[i]:
                    r -= 1
                else:
                    if arr[l] != arr[r]:
                        tmp += 2 * count[arr[l]] * count[arr[r]]
                    else:
                        tmp += count[arr[l]] * count[arr[r]]
                    l += 1
                    r -= 1
            count[arr[i]] = tmp % (10**9 + 7)
            res += tmp
        return res % (10**9 + 7)