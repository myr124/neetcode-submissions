class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        window = set()
        for R in range(len(s)):
            while s[R] in window:
                print(s[L:R])
                
                window.remove(s[L])
                L += 1
            window.add(s[R])
            length = max(length, R-L+1)

        return length

            
            
            
