class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def backtrack(sub, res, i):
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), res, i+1)
                backtrack(sub + s[i], res, i+1)
        backtrack("", res, 0)
        return res