class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cd = collections.Counter(text)
        return min(cd['b'], cd['a'], cd['l']//2, cd['o']//2, cd['n'])