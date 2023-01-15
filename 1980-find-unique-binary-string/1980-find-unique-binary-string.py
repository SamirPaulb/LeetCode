class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numset = set(nums)
        for num in nums:
            num = list(num)
            for i in range(len(num)):
                arr = num
                if arr[i] == '0':
                    arr[i] = '1'
                else:
                    arr[i] = '0'
                ans = "".join(arr)
                if ans not in numset: return ans
        
        return ""