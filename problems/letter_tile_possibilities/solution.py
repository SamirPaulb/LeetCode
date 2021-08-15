class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = []
        def dfs(path, t):
            if path:
                res.append(path)
            for i in range(len(t)):
                dfs(path + t[i], t[:i]+t[i+1:])
            return res
        dfs("", tiles)
        return len(set(res))