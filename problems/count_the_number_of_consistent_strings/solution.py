class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        P = 0
        for i in range(len(words)):
            words[i] = set(words[i])
            words[i] = list(words[i])
            s = 0
            for j in range(len(words[i])):
                if words[i][j] in allowed:
                    s +=1
            if s == len(words[i]):
                P +=1
                
        return P
                