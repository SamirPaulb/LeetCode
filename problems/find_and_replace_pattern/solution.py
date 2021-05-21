class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans, codex = [], defaultdict()
        def translate(c: str) -> str:
            if c not in codex:
                codex[c] = chr(97 + len(codex))
            return codex[c]
        def compare(word: str) -> None:
            codex.clear()
            for i in range(len(word)):
                if translate(word[i]) != cipher[i]:
                    return
            ans.append(word)
        cipher = [translate(c) for c in pattern]
        for word in words:
            compare(word)
        return ans
