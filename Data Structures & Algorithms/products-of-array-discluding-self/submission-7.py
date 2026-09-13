# integer array nums
# return an array output
# where output[i] is the product of all the elements of nums except nums[i]

#follow-up: could you solve this in o(n) time without division?


# prefix arrays
# suffix arrays


# [1,2,4,6]
# [1,1,2,8]
# [48,24,6,1]
# 48, 24, 12, 8




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # o(n) == o(n)
        prefixNum = 1
        suffixNum = 1
        suffix = []
        prefix = []

        for i in range(len(nums)): # prefix
            if i == 0:
                prefix.append(prefixNum)
                continue
            prefixNum *= nums[i-1]
            prefix.append(prefixNum)
        
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                suffix.append(suffixNum)
                continue
            suffixNum *= nums[i+1]
            suffix.insert(0,suffixNum)
        
        output = []

        for i in range(len(nums)):
            output.append(suffix[i]*prefix[i])

        return output      