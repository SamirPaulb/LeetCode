class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        for i in range(len(s)):
            a = ord(s[i])
            if a>=97 and a <= 122 or a>=48 and a<=57 or a>=65 and a<=90:
                news += s[i]
        news = news.lower()
        revs = news[::-1]
        return revs == news
    