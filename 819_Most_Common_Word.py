class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # https://leetcode.com/problems/most-common-word/discuss/193268/python-one-liner
        banned = set(banned)
        count = collections.Counter(word for word in re.split('[ !?\',;.]',
                                    paragraph.lower()) if word)
        return max((item for item in count.items() if item[0] not in banned),
                   key=operator.itemgetter(1))[0]
