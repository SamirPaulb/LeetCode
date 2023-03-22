ans = 0
for i in range(2, n):
if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
dp[i] = dp[i-1] + 1
ans += dp[i]
return ans
```
​
**Complexity**
​
- Time: `O(N)`, where `N <= 5000` is length of `nums` array.
- Space: `O(N)`
​
---
​
**✔️ Solution 2: Bottom up DP (Space Optimized)**
​
- Since our dp only access current dp state `dp` and previous dp state `dpPrev`.
- So we can easy to achieve O(1) in space.
​
```
class Solution:
def numberOfArithmeticSlices(self, nums: List[int]) -> int:
n = len(nums)
dp, dpPrev = 0, 0
ans = 0
for i in range(2, n):
if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
dp = dpPrev + 1
ans += dp
dpPrev = dp
dp = 0
return ans
```
​
**Complexity**
​
- Time: `O(N)`, where `N <= 5000` is length of `nums` array.
- Space: `O(1)`