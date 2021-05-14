class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a = s.split()
        result = ""
        for i in range(k):
            result = result + a[i] + " "
        
        return result.rstrip(" ")