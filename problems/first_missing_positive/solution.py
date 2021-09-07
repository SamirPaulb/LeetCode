class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a = [False]*(10**6) # This array will take constant space as length of this array is not dependent on the length of given array. 
        # A Boolean takes 1 Bit only So if we take a boolean array it will take 32 times less space than integer array; as an integer takes 4 Bite = 4*8 Bit = 32 Bit
        for i in nums:
            if i > 0 and i < len(a):
                a[i-1] = True
        #print(a)
        for i in range(len(a)):
            if a[i] == False:
                return i + 1