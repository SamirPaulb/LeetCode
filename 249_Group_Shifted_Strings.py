class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strings:
            key = self.hashCode(s)
            try:
                dic[key].append(s)
            except KeyError:
                dic[key] = [s]
        return dic.values()

    def hashCode(self, string):
        if string is None or len(string) == 0:
            return ''
        if len(string) == 1:
            return 'a'
        step = abs(ord(string[0]) - ord('a'))
        if step == 0:
            return string
        key = 'a'
        for ch in string[1:]:
            curr = ord(ch) - step
            if ord(ch) - step < ord('a'):
                curr += 26
            key += chr(curr)
        return key
