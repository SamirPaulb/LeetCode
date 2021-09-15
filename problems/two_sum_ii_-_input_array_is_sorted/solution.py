class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, ch in enumerate(numbers): 
            n = target - ch
            if n not in dic:
                dic[ch] = i
            else:
                return [dic[n]+1, i+1]