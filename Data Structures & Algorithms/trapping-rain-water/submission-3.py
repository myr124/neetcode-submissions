'''
- two pointers
- [0,2,1,1,2,3,1,0,1,3,2,1]
                     ^   ^ 

conditionals
- if both walls are smaller than middle then move window
- if left if bigger than middle but right is not keep moving right until it is bigger or no more values
    - calculate area
- we check if right after is bigger if so we move the pointer to right
    - calculate area (maybe use a helper here)
- if right is smaller we reset our window and repeat above process


- we kinda understood how to maybe use the two pointer technique here
- we definitely know how to calculate area



- min(height)

  x    X
X x    X
X x    X
  o

- taking three arrays maxleft, maxright and min of those and he made that one operation with two pointers
'''


class Solution:
    def trap(self, height: List[int]) -> int:


        l = 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]

        res = 0

        while l < r:

            if leftMax <= rightMax:
                l+=1
                leftMax = max(height[l],leftMax)
                res += leftMax - height[l]
            else:
                r-=1
                rightMax = max(height[r],rightMax)
                res+= rightMax - height[r]
        
        return res
               
        