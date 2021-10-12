class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumDic = {0 : -1}
        current_sum = 0
        for i, ch in enumerate(nums):
            current_sum += ch
            if k != 0:
                current_sum = current_sum % k
            if current_sum in sumDic:
                 # I know that sum between mp[prefix_sum] + 1 and i is multiple of K, so I don't have to include mp[prefix_sum]
                if i - sumDic[current_sum] >= 2:
                    return True
            # if prefix_sum doesn't exists, then add its index, otherwise don't update it, i would always prefer to keep the
            # oldest index, so that I can get length of atleast 2
            else:
                sumDic[current_sum] = i
        
        return False