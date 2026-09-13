class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        alphabet = defaultdict(int)
        maxf = 0
        res = 0
        #XYYX
        for r in range(len(s)):
            alphabet[s[r]] += 1
            while (r-l+1) - max(alphabet.values()) > k:
                alphabet[s[l]]-=1
                l+=1
                
            
            res = max(res, r-l+1)
            
        
        return res

        