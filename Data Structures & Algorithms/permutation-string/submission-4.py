class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        windowSize = len(s1)-1
        L = 0
        R = 0

        s1freq = {}
        s2freq = {}

        for c in s1:
            s1freq[c] = 1 + s1freq.get(c, 0)

        for R in range(len(s2)):
            
            if s2[R] in s1freq:
                s2freq[s2[R]] = 1 + s2freq.get(s2[R],0)
            
            if R-L > windowSize:
                if s2[L] in s1freq:
                    s2freq[s2[L]] = s2freq.get(s2[L],0) - 1
                L+=1
            
            if s2freq == s1freq:
                return True
        

        return False



        