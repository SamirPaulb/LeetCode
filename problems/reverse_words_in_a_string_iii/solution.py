class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        ls = []
        for i in range(len(s)):
            if s[i] != " ":
                ls.append(s[i])
            if s[i] == " ":
                a = len(ls)
                for j in range(a):
                    ans += ls[-1]
                    ls.pop(-1)
                ans += " "
            if i == len(s) - 1:
                a = len(ls)
                for j in range(a):
                    ans += ls[-1]
                    ls.pop(-1)
        return ans