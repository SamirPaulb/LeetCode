class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        L_ind, R_ind, ans = -1, -1, 0
        for i, num in enumerate(A):
            if num >= L: L_ind = i
            if num > R:  R_ind = i
            ans += L_ind - R_ind
        return ans