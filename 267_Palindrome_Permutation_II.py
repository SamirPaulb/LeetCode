class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        half = []
        res = []
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        odd, even = 0, 0
        for c in dic:
            if dic[c] % 2 == 0:
                even += 1
            else:
                odd += 1
        if odd > 1:
            return []
        # generate half
        seed = []
        mid = ''
        for c in dic:
            if dic[c] % 2 == 1:
                mid = c
            seed.extend([c] * (dic[c] / 2))
        self.permute(half, seed, 0)
        # merge half to get res
        for r in half:
            res.append(''.join(r) + mid + ''.join(reversed(r)))
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
