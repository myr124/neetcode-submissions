'''

- integers cost where cost[i] is the cost of taking a step (or two) from ith
floor of a staircase 

- You may choose to start at the index 0 or the index 1 floor.

- return min cost to reach top of staircase just past last index in cost

return min cost to reach past end of array with an array of costs, each step
can cover one or two steps

recursive fun(i, cost):
    base condition of being past len(costs):
        return cost
    
    onestep = fun(i+1, cost + cost[i])
    twostep = fun(i+2, cost + cost[i])

    return min(onestep, twostep)

    now time to optimize

    can we cache? yes i believe so, there are tons of repeated operations
    so we can create a memoization solution and store values in a cache

'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = [-1] *len (cost)
        def rec(i):
            if i > len(cost)-1:
                return 0

            if cache[i] != -1:
                return cache[i]
            
            onestep = cost[i] + rec(i+1)
            twostep = cost[i] + rec(i+2)

            cache[i] = min(onestep,twostep)

            return cache[i]
        
        zero = rec(0)
        print(zero)
        one = rec(1)
        print(one)

        return min(zero,one)
        

        