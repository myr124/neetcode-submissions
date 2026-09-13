class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #hehehehe
        subsets= []
        curset = []  # two global lists one that holds subset being built and the other holds all subsets

        def helper(nums,i, curset, subsets):
            if i >= len(nums):
                subsets.append(curset.copy())
                return
            
            # Decision to include value
            curset.append(nums[i])
            helper(nums,i+1,curset, subsets)
            curset.pop()

            # Decision to not include value
            helper(nums,i+1, curset, subsets)

        helper(nums,0,curset, subsets)
        return subsets
        
        