class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1:
            return True
        for i in range(len(arr)):
            if (arr[i] /2 in arr or arr[i] *2 in arr )and arr[i] != 0:
                return True
        return False