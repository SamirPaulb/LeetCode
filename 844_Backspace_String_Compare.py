class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if S == T:
            return True
        s_stack = []
        t_stack = []
        for c in S:
            if c != '#':
                s_stack.append(c)
            elif len(s_stack) != 0:
                s_stack.pop(-1)
        for c in T:
            if c != '#':
                t_stack.append(c)
            elif len(t_stack) != 0:
                t_stack.pop(-1)
        return ''.join(s_stack) == ''.join(t_stack)

    # def backspaceCompare(self, S, T):
    #     # https://leetcode.com/problems/backspace-string-compare/discuss/135603/C%2B%2BJavaPython-O(N)-time-and-O(1)-space
    #     back = lambda res, c: res[:-1] if c == '#' else res + c
    #     return reduce(back, S, "") == reduce(back, T, "")

    # def backspaceCompare(self, S, T):
    #     def back(res, c):
    #         if c != '#': res.append(c)
    #         elif res: res.pop()
    #         return res
    #     return reduce(back, S, []) == reduce(back, T, [])


    # def backspaceCompare(self, S, T):
    #     i, j = len(S) - 1, len(T) - 1
    #     backS = backT = 0
    #     while True:
    #         while i >= 0 and (backS or S[i] == '#'):
    #             backS += 1 if S[i] == '#' else -1
    #             i -= 1
    #         while j >= 0 and (backT or T[j] == '#'):
    #             backT += 1 if T[j] == '#' else -1
    #             j -= 1
    #         if not (i >= 0 and j >= 0 and S[i] == T[j]):
    #             return i == j == -1
    #         i, j = i - 1, j - 1
