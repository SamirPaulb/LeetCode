class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # return [s[:i] + "--" + s[i+2:] for i in range(len(s) - 1) if s[i] == s[i + 1] == "+"]
        res = []
        if s is None or len(s) == 0:
            return res
        ls = len(s)
        for i in range(ls - 1):
            if s[i] == '+' and s[i + 1] == '+':
                res.append(s[:i] + '--' + s[i + 2:])
        return res
