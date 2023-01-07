class Solution:
    def maxProduct(self, words: List[str]) -> int:
        wordDict = {word:[False]*26 for word in words}
        for word in words:
            for w in word:
                wordDict[word][ord(w) - 97] = True
        
        res = 0
        for i, w1 in enumerate(words):
            for w2 in words[i+1:]:
                flag = True
                for j in range(26):
                    if wordDict[w1][j] and wordDict[w2][j]:
                        flag = False
                if flag:
                    res = max(res, len(w1) * len(w2))
        
        return res              