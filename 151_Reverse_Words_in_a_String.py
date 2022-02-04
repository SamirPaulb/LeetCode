class Solution(object):
    # def reverseWords(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     # O(n) and O(n) space
    #     if len(s) == 0:
    #         return s
    #     temp = s.split(' ')
    #     temp = [t for t in temp if len(t) > 0]
    #     temp = reversed(temp)
    #     return ' '.join(temp)

    def reverseWords(self, s):
        # remove tail space
        s = s.strip(' ')
        array_s = []
        last = ' '
        # remove multiple spaces
        for i in range(len(s)):
            if s[i] != ' ':
                array_s.append(s[i])
            else:
                if last != ' ':
                    array_s.append(s[i])
            last = s[i]
        array_s = array_s[::-1]
        ls, pos = len(array_s), 0
        for i in range(ls + 1):
            if i == ls or array_s[i] == ' ':
                self.reverse(array_s, pos, i)
                pos = i + 1
        return ''.join(array_s)

    def reverse(self, array_s, begin, end):
        for i in range((end - begin) / 2):
            array_s[begin + i], array_s[end - i - 1] = array_s[end - i - 1], array_s[begin + i]

