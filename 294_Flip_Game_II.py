class Solution(object):
    # def canWin(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     if s is None or len(s) < 2:
    #         return False
    #     for i in range(len(s) - 1):
    #         if s[i:i + 2] == '++':
    #             if not self.canWin(s[:i] + '--' + s[i + 2:]):
    #                 return True
    #     return False

    def canWin(self, s):
        if s is None or len(s) < 2:
            return False
        list_s = list(s)
        return self.canWin_helper(list_s)

    def canWin_helper(self, s):
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                s[i] = '-'
                s[i + 1] = '-'
                res = self.canWin_helper(s)
                s[i] = '+'
                s[i + 1] = '+'
                if not res:
                    return True
        return False

    # def canWin(self, s):
    #     # backtracking with memo
    #     memo = {}

    #     def can(s):
    #         if s not in memo:
    #             memo[s] = any(s[i:i + 2] == '++' and not can(s[:i] + '-' + s[i + 2:])
    #                           for i in range(len(s)))
    #         return memo[s]
    #     return can(s)
    # https://discuss.leetcode.com/topic/27282/theory-matters-from-backtracking-128ms-to-dp-0ms/3
    # def canWin(self, s):
    #     g, G = [0], 0
    #     for p in map(len, re.split('-+', s)):
    #         while len(g) <= p:
    #             g += min(set(range(p)) - {a^b for a, b in zip(g, g[-2::-1])}),
    #         G ^= g[p]
    #     return G > 0

    # def canWin(self, s):
    #     currlen, maxlen = 0, 0
    #     board_ini_state = []
    #     for i in range(len(s)):
    #         if s[i] == '+':
    #             currlen += 1
    #         if i + 1 == len(s) or s[i] == '-':
    #             if currlen >= 2:
    #                 board_ini_state.append(currlen)
    #             maxlen = max(maxlen, currlen)
    #             currlen = 0
    #     g = [0] * (maxlen + 1)
    #     for l in range(2, maxlen + 1):
    #         gsub = set()
    #         for len_first_game in range(l / 2):
    #             len_second_game = l - len_first_game - 2
    #             gsub.add(g[len_first_game] ^ g[len_second_game])
    #         g[l] = firstMissingNumber(gsub)
    #     g_final = 0
    #     for state in board_ini_state:
    #         g_final ^= g[state]
    #     return g_final != 0

    # def firstMissingNumber(lut):
    #     ls = len(lut)
    #     for i in range(ls):
    #         if i not in lut:
    #             return i
    #     return ls

if __name__ == '__main__':
    s = Solution()
    print s.canWin("++++")
