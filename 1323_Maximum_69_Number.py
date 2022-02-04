class Solution:
    def maximum69Number (self, num: int) -> int:
        # Replace first 6 with 9 if exists
        return(str(num).replace('6', '9', 1))
