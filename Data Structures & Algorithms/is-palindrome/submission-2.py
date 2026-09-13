class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()
        formatString = ""
        for i in s:
            if i.isalnum():
                formatString += i.lower()
        print(formatString)
        L = 0
        R = len(formatString) - 1
        res = True

        while L < R:
            if formatString[L] != formatString[R]:
                res = False
            
            L +=1
            R -=1
        return res