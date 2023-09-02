class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        visited = set()
        visited.add("")
        res = ""
        for word in words:
            if word[:-1] in visited:
                if len(word) > len(res):
                    res = word
                visited.add(word)
        return res