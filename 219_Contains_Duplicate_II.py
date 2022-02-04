class Solution(object):
    # def containsNearbyDuplicate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     """
    #     check = {}
    #     for i in range(len(nums)):
    #         try:
    #             check[nums[i]].append(i)
    #         except:
    #             check[nums[i]] = [i]
    #     # hash all value with its index
    #     # then check the difference between indexes under the same value
    #     for _, v in check.items():
    #         if len(v) >= 2:
    #             pos = 0
    #             while pos + 1 < len(v):
    #                 if v[pos + 1] - v[pos] <= k:
    #                     return True
    #                 pos += 1
    #     return False

    def containsNearbyDuplicate(self, nums, k):
        # check k interval
        check = set()
        for i in range(len(nums)):
            if i > k:
                check.remove(nums[i - k - 1])
            if nums[i] in check:
                return True
            else:
                check.add(nums[i])
        return False

