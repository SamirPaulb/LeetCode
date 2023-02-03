class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        arr = ["" for _ in range(numRows)]
        i = j = 0
        while i < len(s):
            while j < numRows and i < len(s):
                arr[j] += s[i]
                j += 1
                i += 1
            j -= 2
            while j >= 0 and i < len(s):
                arr[j] += s[i]
                j -= 1
                i += 1
            j += 2
        
        return "".join(arr)
                