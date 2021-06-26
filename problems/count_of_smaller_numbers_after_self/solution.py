from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums):
        SList, ans = SortedList(), []
        for num in nums[::-1]:
            ind = SortedList.bisect_left(SList, num)
            ans.append(ind)
            SList.add(num)
            
        return ans[::-1]
