'''
nums where nums[i] represents money that i house has
arranged in straight line
you can rob any house but adjacent ones


nums= [1,1,3,3]

dp[0] = 1
dp[1] = 1
dp[2] = 3+1 = 4
dp[3] = 3+ 1 = 4

dp

'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        if len(nums) < 2:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])


        return dp[-1]


        
        