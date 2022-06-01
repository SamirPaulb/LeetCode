class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {chr(i) : 0 for i in range(97, 123)}   # creating dictionary key as 'a' to 'z' and value as frequency of charecters in s
        for i in s:
            dicS[i] += 1                              # increasing the count of current charecter i
        
        dicT = {chr(i) : 0 for i in range(97, 123)}   # creating dictionary key as 'a' to 'z' and value as frequency of charecters in t
        for i in t:
            dicT[i] += 1                              # increasing the count of current charecter i
        
        return dicS == dicT                           # frequency of charecters in s equal to frequency of charenters in t
		
# Time: O(N)   ; as traversing only once
# Space: O(N)  ; for creating the dictionaries