'''
use ord and char to map frequency of letters in alphabet and compare those to see if equal if so return true 
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force
        # An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
        # carrace vs racecar
        
        

        return sorted(s) == sorted(t)