class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        count = collections.Counter()
        res = 0
        for i in range(len(arr)):
            count[arr[i]] += 1
            tmp = count[arr[i]]
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    tmp += count[arr[j]] * count[arr[i] // arr[j]]
            count[arr[i]] = tmp % (10**9 + 7)
        
        return sum(count.values()) % (10**9 + 7)