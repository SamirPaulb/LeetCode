class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_map = {}
        for c in s:
            count_map[c] = count_map.get(c, 0) + 1
        for i, c in enumerate(s):
            if count_map[c] == 1:
                return i
        return -1

    # def firstUniqChar(self, s):
    #     min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])
