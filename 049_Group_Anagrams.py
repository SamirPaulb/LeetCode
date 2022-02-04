class Solution(object):
    # def groupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     hash = {}
    #     for s in strs:
    #         key = self.hash_key(s)
    #         try:
    #             hash[key].append(s)
    #         except KeyError:
    #             hash[key] = [s]
    #     for k, v in hash.items():
    #         if len(v) > 1:
    #             # sort
    #             v.sort()
    #     return hash.values()
    #
    # def hash_key(self, s):
    #     # hash string with 26 length array
    #     table = [0] * 26
    #     for ch in s:
    #         index = ord(ch) - ord('a')
    #         table[index] += 1
    #     return str(table)

    def groupAnagrams(self, strs):
        strs.sort()
        hash = {}
        for s in strs:
            key = self.hash_key(s)
            try:
                hash[key].append(s)
            except KeyError:
                hash[key] = [s]
        return hash.values()

    def hash_key(self, s):
        # hash string with 26 length array
        table = [0] * 26
        for ch in s:
            index = ord(ch) - ord('a')
            table[index] += 1
        return str(table)