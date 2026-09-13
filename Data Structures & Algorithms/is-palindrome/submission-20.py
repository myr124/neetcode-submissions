'''
brute force: go through entire string remove non alphanum chars

reverse string and then compare

Alphanumeric

O(n)

O(n)

Optimized Two Pointer approach:

- two while loops one for l and one for r just keep pushing pointers until we hit a alphanumeric character
- two pointer has to be matching at every alphanum instance


runtime complexity:

O(n)

space complexity:

O(1)

l, r = o(1)

alphabet = "abcdesadasdasdadadadadad"

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l,r = 0, len(s)-1

        while l < r:

            while not s[l].isalnum() and l < r:
                l+=1
            while not s[r].isalnum() and r > l:
                r-=1
            

            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1

            
        return True


