class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        return [k for k,v in counter.most_common(k)]
        # return heapq.nlargest(k, count.keys(), key=count.get)
