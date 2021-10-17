import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myHeap = []
        for i in nums:
            heapq.heappush(myHeap, i)
        
        prev = None
        sequence = 0
        max_sequence = 0
        while myHeap:
            cur_num = heapq.heappop(myHeap)
            if prev == None:
                sequence = 1
            elif prev != None and cur_num - prev == 1:
                sequence += 1
            elif prev == cur_num:
                continue
            else:
                sequence = 1
            
            prev = cur_num
            max_sequence = max(max_sequence, sequence)
        
        return max_sequence