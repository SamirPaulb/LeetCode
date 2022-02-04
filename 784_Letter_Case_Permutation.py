class Solution(object):
    # def letterCasePermutation(self, S):
    #     ans = [[]]

    #     for char in S:
    #         n = len(ans)
    #         if char.isalpha():
    #             # Double the ans
    #             for i in xrange(n):
    #                 ans.append(ans[i][:])
    #                 ans[i].append(char.lower())
    #                 ans[n + i].append(char.upper())
    #         else:
    #             # Normal append
    #             for i in xrange(n):
    #                 ans[i].append(char)

    #     return map("".join, ans)

    def letterCasePermutation(self, S):
        B = sum(letter.isalpha() for letter in S)
        ans = []

        for bits in xrange(1 << B):
            b = 0
            word = []
            for letter in S:
                if letter.isalpha():
                    if (bits >> b) & 1:
                        word.append(letter.lower())
                    else:
                        word.append(letter.upper())

                    b += 1
                else:
                    word.append(letter)

            ans.append("".join(word))
        return ans
