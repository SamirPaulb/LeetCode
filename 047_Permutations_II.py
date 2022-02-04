class Solution(object):
    # def __init__(self):
    #     self.result = {}
    #
    # def permuteUnique(self, num):
    #     """
    #         :type nums: List[int]
    #         :rtype: List[List[int]]
    #         """
    #     if num is None:
    #         return []
    #     num.sort()
    #     self.getPermute([], num)
    #     return self.result.values()
    #
    # def getPermute(self, prefix, rest):
    #     ls = len(rest)
    #     if ls == 0:
    #         return
    #     elif ls == 1:
    #         temp = prefix + rest
    #         stemp = ''.join(str(t) for t in temp)
    #         self.result[stemp] = temp
    #     else:
    #         for i in range(ls):
    #             if i + 1 < ls and rest[i] == rest[i + 1]:
    #                 continue
    #             temp = prefix[:]
    #             temp.append(rest[i])
    #             self.getPermute(temp, rest[:i] + rest[i + 1:])

    def permuteUnique(self, num):
        res = []
        if len(num) == 0:
            return res
        self.permute(res, num, 0)
        return res

    def permute(self, res, num, index):
        if index == len(num):
            res.append(list(num))
            return
        appeared = set()
        for i in range(index, len(num)):
            if num[i] in appeared:
                continue
            appeared.add(num[i])
            num[i], num[index] = num[index], num[i]
            self.permute(res, num, index + 1)
            num[i], num[index] = num[index], num[i]

    def permuteUnique(self, num):
        # iterative solution
        res = [[]]
        for i in range(len(nums)):
            cache = set()
            while len(res[0]) == i:
                curr = res.pop(0)
                for j in range(len(curr) + 1):
                    # generate new n permutations from n -1 permutations
                    new_perm = curr[:j] + [nums[i]] + curr[j:]
                    stemp = ''.join(map(str, new_perm))
                    if stemp not in cache:
                        cache.add(stemp)
                        res.append(new_perm)
        return res

