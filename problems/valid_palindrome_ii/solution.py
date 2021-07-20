class Solution:
    def validPalindrome(self, s: str) -> bool:
        def varify(s,i,j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return varify(s,i+1,j) or varify(s,i,j-1)
        return True