class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = list(str(n))
        fst = -1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] < arr[i+1]:
                fst = i
                break
        if fst == -1: return -1
        scd = -1
        for i in range(len(arr)-1, fst, -1):
            if arr[i] > arr[fst]:
                scd = i
                break
        if scd != -1:
            arr[fst], arr[scd] = arr[scd], arr[fst]
        arr[fst+1:] = arr[fst+1:][::-1]
        ans = int(''.join(arr))
        if ans < 2**31: return ans
        return -1