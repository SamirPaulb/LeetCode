class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for i in range(len(arr)):
                A = [arr[i:j+1] for j in range(i,len(arr))  ] 
                for a in A:
                    if len(a)%2 !=0:
                        s += sum(a)
        return s


