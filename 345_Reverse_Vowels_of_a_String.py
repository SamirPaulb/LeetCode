class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_index = []
        vowel = []
        res = []
        pos = -1
        for index, value in enumerate(s):
            if value in 'aeiouAEIOU':
                str_index.append(-1)
                vowel.append(value)
            else:
                str_index.append(index)
        for index in str_index:
            if index < 0:
                res.append(vowel[pos])
                pos -= 1
            else:
                res.append(s[index])
        return ''.join(res)

