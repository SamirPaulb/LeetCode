class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = [[a, 'a'], [b, 'b'], [c, 'c']]
        res = ""
        while True:
            arr.sort()
            i = 1 if len(res) > 1 and res[-2] == res[-1] == arr[2][1] else 2
            if arr[i][0]:
                res += arr[i][1]
                arr[i][0] -= 1
            else:
                break
        
        return res