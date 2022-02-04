class Solution(object):
    # def totalFruit(self, tree):
    #     """
    #     :type tree: List[int]
    #     :rtype: int
    #     """
    #     basket, res, start = 2, 0, 0
    #     queue_map = {}
    #     for i, v in enumerate(tree):
    #         queue_map[v] = queue_map.get(v, 0) + 1
    #         if len(queue_map) > 2:
    #             queue_map[tree[start]] -= 1
    #             if queue_map[tree[start]] == 0:
    #                 del queue_map[tree[start]]
    #             start += 1
    #         res = max(res, i - start + 1)
    #     return res

    # https://leetcode.com/problems/fruit-into-baskets/solution/
    # def totalFruit(self, tree):
    #     blocks = [(k, len(list(v)))
    #               for k, v in itertools.groupby(tree)]
    #     ans = i = 0
    #     while i < len(blocks):
    #         # We'll start our scan at block[i].
    #         # types : the different values of tree[i] seen
    #         # weight : the total number of trees represented
    #         #          by blocks under consideration
    #         types, weight = set(), 0

    #         # For each block from i and going forward,
    #         for j in xrange(i, len(blocks)):
    #             # Add each block to consideration
    #             types.add(blocks[j][0])
    #             weight += blocks[j][1]
    #             # If we have 3 types, this is not a legal subarray
    #             if len(types) >= 3:
    #                 i = j-1
    #                 break
    #             ans = max(ans, weight)
    #         # If we go to the last block, then stop
    #         else:
    #             break
    #     return ans

    def totalFruit(self, tree):
        ans = i = 0
        count = collections.Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
