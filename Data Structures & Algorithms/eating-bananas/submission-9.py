'''
integer array piles
piles[i] is number of bananas in ith pile
integer h which represents the number of hours you have to eat all

k = bananas per hour

return min k 


Input: piles = [1,4,3,2], h = 9
1 + 2 + 2 + 1

5+3+2

1+ 4 + 3 + 2 > 10

1-4 range
do binary search we find middle check if middle is less than hours if so decrease if not increase


Output: 2

Input: piles = [25,10,23,4], h = 4

Output: 25


You should aim for a solution with O(nlogm) time and O(1) space, where n is the size of the input array, and m is the maximum value in the array.

[1,4,3,2]

Input: piles = [25,10,23,4], h = 4

4-25

8

o(nlogm)

o(n)

nlogn

binary search

8
4 2 3 1

10

O(nlogm)

Output: 25


'''


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = float('inf')
        

        while l<=r:
            m = (l+r) // 2
            
            hours = 0

            for i in piles:
                hours += math.ceil(i/m)
            
            print(hours)

            if hours <= h:
                r = m-1
                res = min(m,res)

            elif hours > h:
                l = m+1
        
        return res

            
            
        