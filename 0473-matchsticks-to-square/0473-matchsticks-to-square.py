class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4: return False
        nums.sort(reverse = True)
        side = sum(nums) // 4
        if side*4 != sum(nums): return False
        sideArr = [0] * 4
        
        def dfs(i):
            if i == len(nums):
                return sideArr[0] == sideArr[1] == sideArr[2] == sideArr[3] == side
            for j in range(4):
                if sideArr[j] + nums[i] <= side:
                    sideArr[j] += nums[i]
                    if dfs(i+1):
                        return True
                    sideArr[j] -= nums[i]
            return False
        
        return dfs(0)