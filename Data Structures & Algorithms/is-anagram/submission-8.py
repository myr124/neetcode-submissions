class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = defaultdict(int)
        tDict = defaultdict(int)  

        for i,c in enumerate(s):
           
            sDict[s[i]] += 1
          
            tDict[t[i]] += 1

        return tDict==sDict
        
        