# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """

class Solution(object):
    def longestCommonPrefix(self, strs):
        ls = len(strs)
        if ls == 1:
            return strs[0]
        prefix = ''
        pos = 0
        while True:
            try:
                current = strs[0][pos]
            except IndexError:
                break
            index = 1
            while index < ls:
                try:
                    if strs[index][pos] != current:
                        break
                except IndexError:
                    break
                index += 1
            if index == ls:
                prefix = prefix + current
            else:
                break
            pos += 1
        return prefix

    # def longestCommonPrefix(self, strs):
    #     # https://leetcode.com/discuss/89987/one-line-solution-using-itertools-takewhile
    #     return reduce(lambda s1, s2: ''.join(y[0] for y in itertools.takewhile(lambda x: x[0] == x[1], zip(s1, s2))), strs or [''])



if __name__ == '__main__':
    # begin
    s = Solution()
    print s.longestCommonPrefix(["aca","cba"])