from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        s1map = Counter(s1)
        print(len(s1))
        print(s1map)
        window = ""
       
        
        for r in range(len(s2)):
            print(len(window))
            window += s2[r]
            if len(window)==len(s1):
                print(Counter(window))
                if Counter(window) == s1map:
                    return True
                else:
                    print(window)
                    window = window[1:]
                    print(window)
                    l+=1
        print(window)
        return False


