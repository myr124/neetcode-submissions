# given a string s return true if it is a palindrome, other return false
# palindrome = string that reads same forward and backward
# case insensitive and ignores non-alphanumeric 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")

        print(s)

        start = 0
        end = len(s) - 1

        while start <= end:
            print(start)
            print(end)
            while not s[start].isalnum() and start<len(s)-1:
                start+=1
            while not s[end].isalnum() and end>0:
                end-=1
            
            if (s[start].isalnum() and s[end].isalnum()) and (s[start] != s[end]):
                return False
            
            start+=1
            end-=1


        return True
        