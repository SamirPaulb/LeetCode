class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        time += min((ord(word[0])- ord("a")), (26-(ord(word[0])- ord("a")))) + 1
        for i in range(len(word)-1):
            time += min(abs(ord(word[i+1])-ord(word[i])), (26-abs(ord(word[i+1])-ord(word[i])))) +1
        return time
            