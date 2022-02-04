class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import Queue
        pq = Queue.PriorityQueue(4)
        check = set()
        for n in nums:
            if n in check:
                continue
            pq.put(n)
            check.add(n)
            if len(check) > 3:
                check.remove(pq.get())
        total = len(check)
        while total < 3 and total > 1:
            total -= 1
        return pq.get()
