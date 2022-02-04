class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # check every digit
        return [x for x in range(left, right+1) if all([int(i) != 0 and x % int(i)==0 for i in str(x)])]

    # def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    #     return [x for x in range(left, right+1) if all((i and (x % i==0) for i in map(int, str(x))))]
