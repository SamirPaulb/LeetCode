class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        forward = [0] * len(arr)
        backward = [0] * len(arr)
        
        curr_max, max_so_far = arr[0], arr[0]
        forward[0] = arr[0]
        for index in range(1, len(arr)):
            curr_max = max(arr[index], curr_max + arr[index])
            max_so_far = max(max_so_far, curr_max)
            
            forward[index] = curr_max
            
        curr_max = arr[len(arr) - 1]
        max_so_far = arr[len(arr) - 1]
        backward[len(arr) - 1] = arr[len(arr) - 1]
        
        index = len(arr) - 2
        while index >= 0:
            curr_max = max(arr[index], curr_max + arr[index])
            max_so_far = max(max_so_far, curr_max)
            
            backward[index] = curr_max
            index -= 1
            
        result = max_so_far
        for index in range(1, len(arr)-1):
            result = max(result, forward[index-1] + backward[index + 1])
        return result