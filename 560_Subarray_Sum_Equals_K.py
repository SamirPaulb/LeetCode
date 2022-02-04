class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_map = {}
        sum_map[0] = 1
        count = curr_sum = 0
        for num in nums:
            curr_sum += num
            # Check if sum - k in hash
            count += sum_map.get(curr_sum - k, 0)
            # add curr_sum to hash
            sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1
        return count
