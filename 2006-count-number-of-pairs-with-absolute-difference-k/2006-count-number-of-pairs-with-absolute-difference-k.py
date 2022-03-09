class Solution:
    def countKDifference(self, nums, k):
        seen = defaultdict(int) # make dictionary of integers as key and value as 0
        count = 0
        
        for num in nums:
            count += seen[num-k] + seen[num+k]
            seen[num] += 1
        
        return count
    
'''    
class Solution:
    def countKDifference(self, nums, k):
        seen = {num:0 for num in nums}
        count = 0
        
        for num in nums:
            tmp1 = num - k;  tmp2 = num + k
            if tmp1 in seen:
                count += seen[tmp1]
            elif tmp2 in seen:
                count += seen[tmp2]
            seen[num] += 1
        
        return count
'''