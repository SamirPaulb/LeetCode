class Solution(object):

    def __init__(self):
        self.memo = []
        self.memo.append(0)
        self.memo.append(1)

    def fib(self, N):
        """
        DP with memo
        :type N: int
        :rtype: int
        """
        if N < len(self.memo):
            return self.memo[N]
        for i in range(len(self.memo), N + 1):
            self.memo.append(self.memo[i - 1] + self.memo[i - 2])
        return self.memo[N]

    # def fib(self, N):
    #     """
    #     Recursively, O(n)
    #     :type N: int
    #     :rtype: int
    #     """
    #     if N == 0:
    #         return 0
    #     if N == 1:
    #         return 1
    #     return self.fib(N - 1) + self.fib(N - 2)
