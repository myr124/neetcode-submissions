class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        windowSize = len(s1)-1
        L = 0
        R = 0

        s1freq = [0]*26
        s2freq = [0]*26

        for c in s1:
            s1freq[ord(c)-ord('a')]+=1

        for R in range(len(s2)):
            
            s2freq[ord(s2[R])-ord('a')] += 1
            
            if R-L > windowSize:
                s2freq[ord(s2[L])-ord('a')] -= 1
                L+=1
            
            if s2freq == s1freq:
                return True
        

        return False


        