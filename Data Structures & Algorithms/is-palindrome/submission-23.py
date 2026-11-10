'''
1st approach
we clean up string and make it only alnum characters


2nd approach
we have the regular string and we just ignore characters that dont fall under alnum category


'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        while l <= r:
            
            while not s[l].isalnum() and l < r:
                l+=1
            while not s[r].isalnum() and r > l:
                r-=1

            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
                continue
            
            print(s[l] + s[r])
            return False


        return True



