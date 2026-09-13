'''

permutation - any arrangement but frequencies of letters stay same

compare frequencies?

we make a freqmap of s1
and have a static window of that size
we slide and compare frequencies

abc  {a:1, b:1, c:1}
  
  l r
lecabee {C:1 A:1 B:1} correct return true 

i believe maps are unordered so we can do direct comparison?


'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')] += 1
            count2[ord(s2[i])-ord('a')] += 1
        
        if count1 == count2:
            return True
        
        l = 0

        for r in range(len(s1),len(s2)):
            count2[ord(s2[r])-ord('a')] += 1
            count2[ord(s2[l])-ord('a')] -= 1
            l+=1

            if count1 == count2:
                return True
        
        return False
        