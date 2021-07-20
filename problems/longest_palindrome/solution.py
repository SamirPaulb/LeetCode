class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = set(s)
        a = list(a)
        new = []
        for i in range(len(a)):
            new.append([a[i], s.count(a[i])])
        ans = 0
        k = 0
        for i in range(len(new)):
            if new[i][1] % 2 == 0:
                ans += new[i][1]
            else:
                ans += new[i][1] - 1
                k += 1
        if k > 0:
            return ans +1
        return ans
    