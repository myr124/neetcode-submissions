'''
find longest palindromic substring

given string s return longest ss of s that is a palindrome

what are the properties of a palindrome
bab

  xx
racecar
 xx
bbbb

characters from len(string) and start must equal each other
this can be divided into a subproblems


so determining if a string is a palindrome is simple

but how do apply this to substrings?

we apply this property recursively

then check if its fulfilled

we keep a global array res

apply a recursive function to our string that checks first and last
if equal then we append to our res variable

starting from first and last helps us get the longest ss

pseudocode:


'''


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""
        res = (0,0)


        for i,c in enumerate(s):

            l,r = i,i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 >= res[1]-res[0]+1:
                    res = (l,r)
                l-=1
                r+=1
            
            l,r=i,i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 >= res[1]-res[0]+1:
                    res = (l,r) 
                l-=1
                r+=1
        
        return s[res[0]:res[1]+1]
                
        