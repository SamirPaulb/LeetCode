class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        numLoc = 0
        numGlo = 0

        for i in range(1, len(A)):
            if A[i-1] > A[i]:   # Calculating number of local inversions
                numLoc += 1
                
            if i > A[i]:           # Calculating number of global inversions
                diff = i - A[i]    # diff = actual_index - index_this_value_is_supposed_to_have_if_the_list_is_in_order
                numGlo += diff * (diff + 1) // 2
                # Here checking how many numbers before current number which are greater than this current number
                # A = [6, 3, 2, 1, 0, 4, 5, 7] when i == 5 => A[5] = 0 check how many numbers greater than 0  => we are applying sum of n natural number formule i.e, n*(n-1)/2 as index if from 0 so n == (diff + 1).
        
        return numLoc == numGlo