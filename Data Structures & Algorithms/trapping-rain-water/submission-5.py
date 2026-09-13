'''
- instead of finding windows we check how much water each spot can hold
- we calculate this by finding largest wall on the left and largest on the right
- we take the minimum of these values (setting the boundaries) and then subtract the height
from that point

to find maxleft and maxright for a specific point we can do multiple things
- we can start with an extra space solution
- have two arrays maxleft maxright
- keep a running max for them and populate what the max is at each point
- we also need a min arr that takes the min of these two points

we then can just subtract height at point from this and add to our res

'''


class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        maxRight = [0] *len(height)
        res = 0
        maxVal = height[0]

        for i in range(1,len(height)):
            maxLeft[i] = maxVal
            if height[i] > maxVal:
                maxVal = height[i]
        
        maxVal = height[-1]

        for i in range(len(height)-2, 0,-1):
            print(i)
            maxRight[i] = maxVal
            if height[i] > maxVal:
                maxVal = height[i]

        print(maxLeft)
        print(maxRight)
        
        for i,k in enumerate(height):
            res += max(0,min(maxLeft[i],maxRight[i]) - k)
        
        print(maxRight)
        print(res)
        return res

