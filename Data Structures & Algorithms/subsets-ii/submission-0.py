class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sorts list so duplicate values are adjacent
        curset = []
        subsets = []

        def helper(nums, i, curset, subsets):
            if i >= len(nums):
                subsets.append(curset.copy())
                return
            
            # Decision to include
            curset.append(nums[i])
            helper(nums,i+1, curset, subsets)
            curset.pop()

            # Decision to not include
            while i+1<len(nums) and nums[i+1] == nums[i]:
                i+=1
            helper(nums, i+1, curset, subsets)
        
        helper(nums, 0, curset, subsets)
        return subsets