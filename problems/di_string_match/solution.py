class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = len(s)
        f = 0
        arr = []
        for i in range(len(s)):
            if s[i] == "I":
                arr.append(f)
                f +=1
            else:
                arr.append(l)
                l -= 1
        arr.append(f)
        return arr
    