class Solution(object):
    # def hIndex(self, citations):
    #     """
    #     :type citations: List[int]
    #     :rtype: int
    #     """
    #     # Sort and check the max h where the number of paper with no less than h citations
    #     # is no less than h
    #     citations.sort()
    #     ls = len(citations)
    #     h = ls
    #     while h > 0 and citations[ls - h] < h:
    #             h -= 1 
    #     return h

    # def hIndex(self, citations):
    #     citations.sort()
    #     i = 0
    #     while i < len(citations) and citations[len(citations) - 1 - i] > i:
    #         i += 1
    #     return i

    def hIndex(self, citations):
        # counting sort
        ls = len(citations)
        papers = [0] * (ls + 1)
        for c in citations:
            papers[min(ls, c)] += 1
        k, s = ls, papers[ls]
        while k > s:
            k -= 1
            s += papers[k]
        return k