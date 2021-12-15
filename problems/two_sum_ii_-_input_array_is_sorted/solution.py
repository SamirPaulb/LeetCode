class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: return 
        '''
        dic = {}
        for i, ch in enumerate(numbers):
            rem = target - ch
            if rem in dic:
                return [dic[rem], i + 1]
            dic[ch] = i + 1
        '''
        # Two Pointer Method
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target: l += 1
            elif s > target: r -= 1
            else:
                return [l + 1, r + 1]
                