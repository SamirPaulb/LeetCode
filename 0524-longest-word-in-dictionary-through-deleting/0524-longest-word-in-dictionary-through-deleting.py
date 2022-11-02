class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubciquence(s, a):
            i = 0; j = 0
            while i < len(s) and j < len(a):
                if s[i] == a[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == len(a)

        res = ""
        for a in dictionary:
            if isSubciquence(s, a):
                if not res: res = a
                elif len(a) == len(res) and a < res: res = a
                elif len(a) > len(res): res = a
            # print(res)
        return res
                    