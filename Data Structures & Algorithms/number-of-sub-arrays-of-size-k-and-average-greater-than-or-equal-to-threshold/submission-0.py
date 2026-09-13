class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        L = 0
        window = set()
        windowSum = 0
        res = 0
        for R in range(len(arr)):
            windowSum+= arr[R]
            if R - L + 1 == k:
                if windowSum/k >= threshold: 
                    res+=1
                windowSum -= arr[L]
                L+=1
        
        return res
            

        