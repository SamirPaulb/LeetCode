from collections import defaultdict,Counter,deque















from sys import stdin,stdout,setrecursionlimit




















from math import *






from bisect import bisect_left,bisect_right




from statistics import mode






from functools import reduce







import operator as op


class Solution:
    
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        
        
        


        I   = lambda : stdin.readline().rstrip('\r\n')
        
        
        
        
        
        
        
        
        
        
        
        
        ari = lambda : list(map(int,I().split()))
        ars = lambda : list(map(str,I().split()))
        arf = lambda : list(map(float,I().split()))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        mpi = lambda : map(int,I().split())
        mps = lambda : map(str,I().split())
        mpf = lambda : map(float,I().split())


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        mod = 10**9+7
        setrecursionlimit(10**8)
        inf = float('inf')


        
        def power(A, B, p):

            res = 1  # Initialize result
            A = A % p  # Update A if it is more , than or equal to p

            if A == 0:
                return 0

            while B > 0:

                if (B & 1) == 1:  # If B is odd, multiply, A with result
                    res = (res * A) % p

                B = B >> 1  # B = B/2
                A = (A * A) % p

            return res

        def isPrime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            for i in range(5, ceil(sqrt(n)) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True

        def nearest2(num):
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

            return int(pow(2,int(log(num,2))))

        def comb(n, r):
            r = min(r, n-r)
            if r < 0: return 0

            numer = reduce(op.mul, range(n, n-r, -1), 1)
            denom = reduce(op.mul, range(1, r+1), 1)
            return numer // denom


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        st = set(supplies)
        ans = []
        c = 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        it = 0
        a = 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        while it < 101:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            for i in range(len(ingredients)):

                D = True

                for j in ingredients[i]:

                    if j not in st:
                        D = False
                        a += 1
                        c -= 6
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        break
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        

                if D:
                    
                    if recipes[i] not in st:
                    
                        ans.append(recipes[i])
                        st.add(recipes[i])
                        a += 100
                        c -= 100
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        

            it += 1
            a -= 30
            c -= 1
            
        return ans