'''
n gas stations along circular route
two integer arrays gas and cost
gas[i] is the amount of gas at the ith station
cost[i] is the amount of gas needed to travel from the ith station to the
(i+1)th station

you have a car that can store unlimited gas, but start with empty tan
return starting gas station's index such that you can travel
around circuit in a clockwise direction

brute force solution 
start a loop that tries to circle around from every station
and sees if thats possible, returns the possible one

while station is not original or we run out of gas
keep on looping

how can we optimize?
we try every station
can we minimize that?
wait
we have costs and gas, lets maybe start from the station that gives us the 
best ratio?
ratio can be calculated by gas/cost
for example
1/2 = terrible we cant go anywhere
2/2 = works but not best
3/4 = again bad
4/1 = great


1/2
2/3
3/2

'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        l = 0

        sum = 0

        diff = []

        totalgas = 0
        totalcost = 0

        for g in range(len(gas)):
            totalgas += gas[g]
            totalcost += cost[g]


        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        
        for r in range(len(diff)):
            if sum < 0:
                sum = 0
                l = r
            
            sum += diff[r]

        return -1 if (totalgas-totalcost<0) else l
            
            

        