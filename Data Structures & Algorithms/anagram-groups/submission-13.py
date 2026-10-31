class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        fingerprints = defaultdict(list)

        for word in strs:
            fingerprint = [0] * 26

            for c in word:
                fingerprint[ord(c)-ord('a')] += 1
            
            fingerprint = tuple(fingerprint)
            fingerprints[fingerprint].append(word)
        


        return list(fingerprints.values())

        