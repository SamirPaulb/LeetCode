class Solution:
    def strangePrinter(self, s: str) -> int:
        N = len(s)
        @cache
        def calc(left, right): 
            if left >= right: 
                return 0
            best = calc(left + 1, right) + 1
            for index in range(left + 1, right + 1): 
                if s[left] == s[index]: 
                    best = min(best, calc(left, index - 1) + calc(index, right))
            return best
        return calc(0, N - 1) + 1