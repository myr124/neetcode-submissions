'''
use ord and char to map frequency of letters in alphabet and compare those to see if equal if so return true 
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        smap = {}
        tmap = {}

        for i in range((ord('z') - ord('a'))+1):
            smap[i] = 0
            tmap[i] = 0
        

        for c in s:
            smap[ord(c)-ord('a')] += 1
        
        for c in t:
            tmap[ord(c)-ord('a')] += 1

        return tmap == smap
        