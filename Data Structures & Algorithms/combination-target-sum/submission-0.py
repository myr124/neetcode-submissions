'''
distinct integer array of nums and target integer
target
your task is to return a list of all unique combs of nums
where chosen numbers sum to target
the same number may be chosen from nums an unlimited number of times

'''

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        curcomb = []
        
        def combine(i, curcomb, s):
           
            
            if s == target:
                # print(s)
                res.append(curcomb.copy())
                return
            
            if i >= len(nums) or s > target:
                return

            curcomb.append(nums[i])
            combine(i, curcomb, s + nums[i])
            curcomb.pop()
            combine(i + 1, curcomb, s)
        
        combine(0, curcomb, 0)

        return res



        