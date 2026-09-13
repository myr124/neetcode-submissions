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
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
                

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

        