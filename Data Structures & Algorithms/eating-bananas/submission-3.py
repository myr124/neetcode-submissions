# find minimum k eating speed to eat all bananas in a time span that is lower than h
# if k is larger than pile it still takes an hour
# the highest k we could use is the largest value in the list
# doing that gurantees each pile taking an hour each
# we could setup a range from 1-max(piles) and perform bs
# the condition for the bs to end would be for the h value
# derived from k to be equal to the h given or as close as it can be


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowerBound = 1
        upperBound = max(piles)
        hours = 0
        res = float("inf")

        while lowerBound <= upperBound:
            hours = 0
            middle = (upperBound + lowerBound)//2

            for pile in piles:
                hours += math.ceil(pile/middle)
            print(hours)
            if hours > h:
                lowerBound = middle + 1
            elif hours <= h:
                res = min(middle, res)
                upperBound = middle - 1
        
        return res

            

            