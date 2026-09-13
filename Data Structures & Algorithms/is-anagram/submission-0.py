class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) is not len(t):
            return False
        slist = list()
        tlist= list()    
        for e in s:
            slist.append(e)
        for e in t:
            tlist.append(e)
        tlist.sort()
        slist.sort()
        for i in range(len(slist)):
            if slist[i] is not tlist[i]:
                return False
        return True    
