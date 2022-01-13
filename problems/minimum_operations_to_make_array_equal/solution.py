class Solution:
    def minOperations(self, n: int) -> int:
        # n = 6
        # arr[i] = (2 * i) + 1
        # arr = [1, 3, 5, 7, 9, 11]
        # elements of arr are sequence of contineous odd natural numbers
        # as every number is odd so (arr[0] + arr[-1]) is even
        # Target is to make every element (arr[0] + arr[-1])//2 two at a time
        start = 1          # arr[0]
        end = 2*(n-1) + 1  # arr[-1]
        target = (start + end) // 2
        
        res = 0
        for i in range(n//2):
            res += target - (2*i + 1)
        
        return res