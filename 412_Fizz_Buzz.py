class Solution(object):
    # def fizzBuzz(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     res = []
    #     for i in range(1, n + 1):
    #         if i % 3 == 0:
    #             if i % 5 == 0:
    #                 res.append('FizzBuzz')
    #             else:
    #                 res.append('Fizz')
    #         elif i % 5 == 0:
    #             res.append('Buzz')
    #         else:
    #             res.append(str(i))
    #     return res

    # def fizzBuzz(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     res = []
    #     for i in range(1, n + 1):
    #         curr = ''
    #         if i % 3 == 0:
    #             curr += 'Fizz'
    #         if i % 5 == 0:
    #             curr += 'Buzz'
    #         if not len(curr):
    #             curr += str(i)
    #         res.append(curr)
    #     return res

    def fizzBuzz(self, n):
        return [str(i) * (i % 3 != 0 and i % 5 != 0) + "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) 
                for i in range(1, n + 1)]
    
    # def fizzBuzz(self, n):
    #     return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
