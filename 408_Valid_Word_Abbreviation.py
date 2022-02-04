class Solution(object):
    # def validWordAbbreviation(self, word, abbr):
    #     """
    #     :type word: str
    #     :type abbr: str
    #     :rtype: bool
    #     """
    #     if word == abbr:
    #         return True
    #     pos1 = pos2 = 0
    #     curr = 0
    #     while pos1 < len(abbr) and pos2 < len(word):
    #         try:
    #             num = int(abbr[pos1])
    #             # start with 0
    #             if num == 0 and curr == 0:
    #                 return False
    #             curr = curr * 10 + num
    #         except ValueError:
    #             if curr > 0:
    #                 pos2 += curr
    #             # when number exceeds the end of word
    #             if pos2 >= len(word):
    #                 return False
    #             curr = 0
    #             if abbr[pos1] != word[pos2]:
    #                 return False
    #             pos2 += 1
    #         pos1 += 1
    #     # abbr ends with number
    #     if curr > 0:
    #         pos2 += curr
    #     if pos1 == len(abbr) and pos2 == len(word):
    #         return True
    #     return False
    def validWordAbbreviation(self, word, abbr):
        pos = curr = 0
        for i in range(len(abbr)):
            try:
                num = int(abbr[i])
                if num == 0 and curr == 0:
                    return False
                curr = curr * 10 + num
            except ValueError:
                pos += curr
                curr = 0
                if pos >= len(word):
                    return False
                if word[pos] != abbr[i]:
                    return False
                pos += 1
        pos += curr
        if pos == len(word):
            return True
        return False


        