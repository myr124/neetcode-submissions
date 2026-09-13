class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = {c:0 for c in s}
        tDict = {e:0 for e in t}  

        for i,c in enumerate(s):
           
            sDict[s[i]] += 1
          
            tDict[t[i]] += 1

        return tDict==sDict
        
        