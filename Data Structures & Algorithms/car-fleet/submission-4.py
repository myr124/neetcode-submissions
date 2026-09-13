'''
there are n cars traveling to destination on a one lane highway

2 arrays
position anmd sped both n length

The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

6 8 10
4 7 10

1,4
3,2
3


3 5 10 3

the position of the car and the speed
if a car is ahead(position) and is going faster(speed) it will always be ahead and a fleet

'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        s = [(p,s) for p,s in zip(position,speed)]
        stack = []

        for p,s in sorted(s)[::-1] :
            stack.append((target-p)/s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        
        return(len(stack))

            
        