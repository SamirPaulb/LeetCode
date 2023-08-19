class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, s, path):
            if s == target:
                res.append(path)
                return
            if s > target or i >= len(candidates):
                return
            dfs(i+1, s + candidates[i], path + [candidates[i]])
            r = i+1
            while r < len(candidates) and candidates[r] == candidates[r-1]:
                r += 1
            dfs(r, s, path)
        
        dfs(0, 0, [])
        return res
            