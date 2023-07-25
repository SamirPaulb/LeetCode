class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()
        sList.reverse()
        return ' '.join(sList)