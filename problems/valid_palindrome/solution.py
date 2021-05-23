class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for i in range(len(s)):
            if (ord(s[i]) >=97 and ord(s[i])<=122 ) or (ord(s[i]) >= 48 and ord(s[i]) <= 57) or (ord(s[i])>=65 and ord(s[i])<=90):
                new += s[i]
        new  = new.lower()
        a = new[::-1]
        return a == new