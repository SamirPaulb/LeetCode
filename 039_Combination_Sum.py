class Solution(object):
    # def combinationSum(self, candidates, target):
    #     """
    #     :type candidates: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """
    #     candidates.sort()
    #     return self.getcombinationSum(candidates, [], 0, target)
    #
    #
    # def getcombinationSum(self, candidates, prefix, curr, target):
    #     if len(prefix) == 0:
    #         max_value = candidates[0]
    #     else:
    #         max_value = prefix[-1]
    #     res = []
    #     for i in range(len(candidates)):
    #         if candidates[i] >= max_value:
    #             if curr + candidates[i] == target:
    #                 res.append(prefix+[candidates[i]])
    #             elif curr + candidates[i] < target:
    #                 res.extend(self.getcombinationSum(candidates, prefix+[candidates[i]], curr + candidates[i], target))
    #             else:
    #                 pass
    #     return res


    def combinationSum(self, candidates, target):
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for i in range(1, target + 1):
            for j in range(len(candidates)):
                if candidates[j] > i:
                    break
                for k in range(len(dp[i - candidates[j]])):
                    temp = dp[i - candidates[j]][k][:]
                    if len(temp) > 0 and temp[-1] > candidates[j]:
                        continue
                    temp.append(candidates[j])
                    dp[i].append(temp)
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum([8,7,4,3], 11)




