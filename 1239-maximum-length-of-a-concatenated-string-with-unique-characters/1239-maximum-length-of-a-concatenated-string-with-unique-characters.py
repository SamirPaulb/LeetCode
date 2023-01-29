#----------------------- Method 1 -----------------------
class Solution:
    def maxLength(self, arr):
        dp = [set()]  # adding an empty set
        for a in arr:
            if len(set(a)) < len(a): continue  # repeated character is string
            a = set(a)
            for c in dp:
                if a & c: continue # intersection of 2 sets is not empty 
                dp.append(a | c)   # adding union of set a and c
        
        return max(len(a) for a in dp)
    
    '''
#----------------------- Method 2 -----------------------
class Solution:
    def maxLength(self, arr):
        unique = ['']
        for a in arr:
            for b in unique:
                if len(a+b) == len(set(a+b)):  # a and b are Mutual Exclusivity
                    unique.append(a+b)
        
        return max(len(a) for a in unique)
    
    
#----------------------- Method 3 -----------------------

            '''