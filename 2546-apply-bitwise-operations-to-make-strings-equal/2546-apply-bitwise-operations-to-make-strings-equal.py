class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return s == target or (int(s) > 0 and int(target) > 0)
        