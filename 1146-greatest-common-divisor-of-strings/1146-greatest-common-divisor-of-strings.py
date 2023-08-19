class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        res = ""
        for i in range(min(n1, n2)):
            d1, d2 = n1//(i+1), n2//(i+1)
            if str1[:i+1]*d1 == str1 and str1[:i+1]*d2 == str2:
                res = str1[:i+1]
        return res