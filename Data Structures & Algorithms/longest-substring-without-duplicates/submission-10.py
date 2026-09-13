'''
Given a string s, find the length of the 
longest substring without duplicate characters.

A substring is a contiguous sequence of characters 
within a string.

- return length of longest contiguous substring that has no repeated chars

Input: s = "zxyzxyz"

Output: 3

'zxy' 'xyz' - possible combinations

brute force - nested loop that iterates through all possible string combinations
how can we keep track of repeated chars? we can use a set or frequency map
the contiguous nature of this actually helps us a lot
the second we run into a character we have already seen we can break the inner loop which actually
prevents this from being o(n^2)






 lr
"zxyzxyz"


"xxxx"

 x y z

res = 0        r
               l
Input: s = "xxxx"

if letter in seen we move 
    left +=1 
    remove character from set

calculate window size

seen.add(letter)



       r
     l

 
"zxyzxyz"

3
Output: 1
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        seen = set()

        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            
            seen.add(s[r])
            res = max(res, r-l +1)
        
        return res

        
        

        
        