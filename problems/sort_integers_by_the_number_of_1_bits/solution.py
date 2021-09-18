class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        myDict = {}
        for i in arr:
            b = str(bin(i))
            b = list(b)
            n = b.count("1")
            myDict[i] = n
        # print(myDict)
        
        for i in range(len(arr)-1): 
            for j in range(len(arr)-1):
                if myDict[arr[j]] > myDict[arr[j+1]]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                elif myDict[arr[j]] == myDict[arr[j+1]]:
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
                