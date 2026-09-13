'''
array nums where nums[i] represents money ith house has, houses
are arranged in circle meaning first house and last house are neighbors
- cannot rob adjacent houses
return max amount of money you can rob without alerting police(adjacent houses)

previous recurrence relation
two choices
do we wanna rob house or not rob house
i am thinking about any differences that may arise here
our base conditions could be the same actually
so dp[0] = nums[0] X dp[0] = max(nums[0],nums[len-1])
and dp[1] = max(nums[0], nums[1])
but also a 


[2,9,8,3,6]
[6,2,9,8,3]

no i think we need to define a new recurrence relation
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        

        def helper(l):
            rob1,rob2 = 0,0
            for n in l:
                newRob = max(rob1+n,rob2)
                rob1 = rob2
                rob2 = newRob
            
            return rob2
        

        firstexcluded = helper(nums[1:n])
        firstincluded = helper(nums[:n-1])

        return max(nums[0],firstexcluded, firstincluded)


        