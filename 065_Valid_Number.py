class Solution(object):
    # def isNumber(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     # remove lead and tail space
    #     s = s.strip()
    #     try:
    #         float(s)
    #         return True
    #     except:
    #         if '.' in s or ' ' in s:
    #             return False
    #         temp = s.split('e')
    #         if len(temp) == 2:
    #             try:
    #                 int(temp[0])
    #                 int(temp[1])
    #             except:
    #                 return False
    #             return True
    #     return False

    def isNumber(self, s):
        s = s.strip()
        ls, pos = len(s), 0
        if ls == 0:
            return False
        if s[pos] == '+' or s[pos] == '-':
            pos += 1
        isNumeric = False
        while pos < ls and s[pos].isdigit():
            pos += 1
            isNumeric = True
        if pos < ls and s[pos] == '.':
            pos += 1
            while pos < ls and s[pos].isdigit():
                pos += 1
                isNumeric = True
        elif pos < ls and s[pos] == 'e' and isNumeric:
            isNumeric = False
            pos += 1
            if pos < ls and (s[pos] == '+' or s[pos] == '-'):
                pos += 1
            while pos < ls and s[pos].isdigit():
                pos += 1
                isNumeric = True
        print pos, ls, isNumeric
        if pos == ls and isNumeric:
            return True
        return False
