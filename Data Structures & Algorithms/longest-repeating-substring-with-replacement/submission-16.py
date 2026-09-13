'''


brute force

   
XYYX

   r
l
AAABABB

r
l
ABCDA



'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        freqMap = defaultdict(int)
        maxFreq = 0

        for r in range(len(s)):
            freqMap[s[r]] += 1
            

            maxFreq = max(maxFreq, freqMap[s[r]])

            curr = s[l]
            while ((r-l) + 1) - maxFreq > k:
                if l < len(s) and s[l] == curr:
                    freqMap[s[l]] -= 1
                    l+=1

            res = max(res, r-l+1)


        return res
                    
'''
    
s="AAABABB"
'''



