class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dq = deque()
        for i in range(len(nums)):
            nums[i] += nums[dq[0]] if len(dq) else 0
            while dq and i - dq[0] >= k: dq.popleft()  # remove expired elements which are earlier than the (i-k)th element
            while dq and nums[i] >= nums[dq[-1]]: dq.pop() # remove elements which are smaller than the current input
            dq.append(i)
        return nums[-1]

        