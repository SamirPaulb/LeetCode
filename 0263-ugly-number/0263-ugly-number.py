# https://youtu.be/M0Zay1Qr9ws

class Solution:
    def isUgly(self, n: int) -> bool:
        # Negative Values are not considerd as ugly numbers.
        if n <= 0: return False
        for p in [2, 3, 5]:
            # An Ugly number is only divided with either 2 or 3 or 5 , to check that , iterated a loop through a fixed array .
            while n % p == 0:
                # This while loop checks the divisibility of number . If satisfied , it divides the p by n , untill p is not divisible ny n anymore . This loop runs for every number in the array.
                n = n // p
                # finally it checks the conditoin , if n equall to one after performing division loop , the ugly number conditions are stasfied . 
        return n == 1
