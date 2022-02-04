class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        move_pos = 0
        last_pos = len(arr) - 1
        for i in range(last_pos + 1):
            # Only check [0, lastPos - movePos]
            if i > last_pos - move_pos:
                break
            if arr[i] == 0:
                # Special case
                if i == last_pos - move_pos:
                    arr[last_pos] = 0
                    last_pos -= 1
                    break
                move_pos += 1
        last_pos -= move_pos
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + move_pos] = 0
                move_pos -= 1
                arr[i + move_pos] = 0
            else:
                arr[i + move_pos] = arr[i]
