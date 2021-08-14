class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlength = 0
        cur_sum = 0
        mydict = {0:-1}
        for i in range(len(nums)):
            cur_sum += 1 if nums[i] == 1 else -1
            if cur_sum in mydict:
                maxlength = max(maxlength, i-mydict[cur_sum])
            else:
                mydict[cur_sum] = i
        return maxlength