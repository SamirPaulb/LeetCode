class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordDict = {}
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                if key not in wordDict:
                    wordDict[key] = [word]
                else:
                    wordDict[key].append(word)
        
        q = collections.deque()
        q.append([beginWord, 1])
        visited = {beginWord}
        while q:
            word, level = q.popleft()
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                if key not in wordDict: continue
                for w in wordDict[key]:
                    if w == endWord: return level + 1
                    if w not in visited:
                        q.append([w, level+1])
                        visited.add(w)
        return 0