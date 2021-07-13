class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        n = max(len(word1), len(word2))
        for i in range(n):
            if len(word1) > i:
                s += word1[i]
            if len(word2) > i:
                s += word2[i]
        return s