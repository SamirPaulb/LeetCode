class Solution:
    def maximumUnits(self, box: List[List[int]], truckSize: int) -> int:
        box.sort(key = lambda x:x[1])
        res = 0
        # print(box)
        while box and truckSize > 0:
            top = box.pop()
            if truckSize >= top[0]:
                res += top[0] * top[1]
                truckSize -= top[0]
            else:
                res += truckSize * top[1]
                break
        
        return res