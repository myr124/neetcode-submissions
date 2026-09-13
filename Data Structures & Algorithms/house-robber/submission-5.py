'''
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
                continue
            elif i == 1:
                dp[i] = max(nums[0],nums[1])
                continue
            
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        print(dp)
        return dp[-1]
        

        
        