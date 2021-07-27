class Solution:
    def fairCandySwap(self, A, B):
        dif = (sum(A) - sum(B)) / 2
        A = set(A)
        for b in set(B):
            if dif + b in A:
                return [dif + b, b]