class Solution(object):
    # def combine(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     candidates = range(1, n + 1)
    #     self.get_combine(res, candidates, [], k, 0)
    #     return res
    #
    # def get_combine(self, res, candidates, prefix, k, start):
    #     # recursive
    #     if k == 0:
    #         res.append(prefix)
    #     for index in range(start, len(candidates)):
    #         self.get_combine(res, candidates,
    #                          prefix + [candidates[index]],
    #                          k - 1, index + 1)

    def combine(self, n, k):
        res = []
        self.get_combine(res, [], n, k, 1)
        return res

    def get_combine(self, res, prefix, n, k, start):
        # recursive with only one array
        if k == 0:
            res.append(list(prefix))
        elif start <= n:
            prefix.append(start)
            self.get_combine(res, prefix,
                             n, k - 1, start + 1)
            prefix.pop()
            self.get_combine(res, prefix,
                             n, k, start + 1)



if __name__ == "__main__":
    s = Solution()
    print s.combine(4, 2)