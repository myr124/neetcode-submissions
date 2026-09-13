# objective find lowest k such that you can eat all the bananas within h hours
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minVal = right
        while left <= right:
            k = (right+left)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/k)

            if hours <= h:
                minVal = (right+left)//2
                right = k-1        
            else:
                left = k+1
            
                        

        return minVal
                

        