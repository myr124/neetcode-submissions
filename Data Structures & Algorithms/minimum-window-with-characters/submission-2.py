'''
given two strings s and t, return shortest substring such that every character in t, including duplicates is present in the ubstring,
if it doesnt exist return empty string. correct output is always unique.

we can grow a window to a get a substring that has all characters
but how do we minimize the length?


l     r
OUZODYXAZV


z:1 x:1 y:1

z:1 x:1 y:1

res =  

frequency map to store frequency of chars



- shortest substring
- includes duplicates

edge case:
if s is smaller than t return ""
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def helper(smap,tmap):
            keycount = 0
            res = 0
            for k in smap:
                if smap[k] >= tmap[k]:
                    res +=1
                keycount +=1
            
            return keycount == res

        l = 0
        tmap = Counter(t)
        smap = {}
        res = (-1,-1)

        for c in t:
            smap[c] = 0

        print(smap)

        for r in range(len(s)):
            if s[r] in smap:
                smap[s[r]] += 1
                print(r)
            while helper(smap,tmap):
                print(smap)
                if res == (-1,-1):
                    res = (l,r)
                elif (r-l + 1) < (res[1] - res[0] + 1):
                    res = (l,r)
                if s[l] in smap:
                    smap[s[l]] -= 1
                l+=1
        

        return s[res[0]:res[1]+1]
                

'''
 l
          r
ADOBECODEBANC

helper function



map = map


AaAbB

            
Input: s = "xyz", t = "xyz"

count = 0

Output: "xyz"
'''

        