class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        
        def dfs(path, tiles):
            if path:
                res.add(path)
            for i in range(len(tiles)):
                dfs(path + tiles[i], tiles[:i] + tiles[i+1:])
        
        dfs("", tiles)
        return len(res)