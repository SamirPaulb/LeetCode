class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/5088/my-ac-is-o-1-space-o-n-running-time-solution-does-anybody-have-posted-this-solution
        ls = len(gas)
        begin, end = 0, ls - 1
        curr = gas[end] - cost[end]
        while begin < end:
            if curr >= 0:
                curr += gas[begin] - cost[begin]
                begin += 1
            else:
                end -= 1
                curr += gas[end] - cost[end]
        if curr >= 0:
            return end
        else:
            return -1

