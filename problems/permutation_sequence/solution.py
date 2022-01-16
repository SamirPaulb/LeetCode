# https://www.youtube.com/watch?v=wT7gcXLYoao
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i+1) for i in range(n)]
        
        if n == 1 or k == 1: return "".join(nums)
        
        fact = math.factorial(len(nums) - 1)
        ans = ""
        k = k-1
        
        while nums:
            n = len(nums) - 1
            i = k // fact
            ans += nums[i]
            if n == 0: break
            nums.pop(i)
            k = k % fact
            fact = fact // n
                
        return ans

# Time Complexity = O(N*N) ; we are traversing nums 1 time but POPPING ELEMENT FROM MIDDLE OF ARRAY TAKES O(N) TIME, AS AFTER POPPING ELEMENTS REARRANGE WITH NEW INDEX. 
# Space Complexity = O(N) ;    for taking nums